import streamlit as st
import traceback

from pages.shared_ui import apply_theme, sidebar

from core.response_generator import ResponseGenerator
from core.performance import PerformanceEngine
from core.responsible_ai import ResponsibleAIEngine
from core.context import ContextEngine
from core.cost import CostEngine
from core.knowledge import KnowledgeBase
from core.policy import PolicyEngine
from core.risk import RiskEngine
from core.confidence import ConfidenceEngine
from core.decision import DecisionEngine

from database.db import save_analysis


# =================================
# PAGE CONFIGURATION
# =================================

st.set_page_config(
    page_title="ControlPlane.ai Response Simulator",
    page_icon="🛡️",
    layout="wide"
)
apply_theme()
sidebar("simulator")


# =================================
# SESSION STATE INITIALIZATION
# =================================

if "generated_response" not in st.session_state:
    st.session_state.generated_response = ""

if "response_source" not in st.session_state:
    st.session_state.response_source = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "last_query" not in st.session_state:
    st.session_state.last_query = ""


# =================================
# CLEAR PREVIOUS RESPONSE
# =================================

def clear_previous_response():

    st.session_state.generated_response = ""

    st.session_state.response_source = ""

    st.session_state.analysis_result = None


# =================================
# PAGE TITLE
# =================================

st.title(
    "🛡️ ControlPlane.ai Response Simulator"
)

st.write(
    "Generate or audit an AI response and evaluate it "
    "through safety, reliability, context, cost, "
    "knowledge grounding, policy compliance, "
    "confidence, and governance checks."
)


# =================================
# AI RESPONSE EVALUATION
# =================================

st.header(
    "📝 AI Response Evaluation"
)


# =================================
# USER QUERY
# =================================

user_query = st.text_area(
    "User Query",
    placeholder=(
        "Example: Should I invest all my savings "
        "in this company's stock?"
    ),
    key="user_query",
    on_change=clear_previous_response
)


# =================================
# APPLICATION CONTEXT
# =================================

application_context = st.selectbox(
    "Application Context",
    [
        "customer_service",
        "finance",
        "healthcare",
        "hr",
        "general"
    ]
)


# =================================
# CLEAR RESPONSE WHEN QUERY IS EMPTY
# =================================

if not user_query.strip():

    st.session_state.generated_response = ""

    st.session_state.response_source = ""

    st.session_state.analysis_result = None


# =================================
# RESPONSE SOURCE
# =================================

st.subheader(
    "Response Source"
)

st.write(
    "Choose how to provide the AI response."
)


response_source = st.radio(
    "Response Source",
    [
        "🤖 Generate AI Response",
        "📂 Enter Existing Response"
    ],
    horizontal=True,
    label_visibility="collapsed"
)


# =================================
# GENERATE AI RESPONSE
# =================================

if response_source == "🤖 Generate AI Response":

    st.info(
        "ControlPlane.ai will generate an AI response "
        "and then evaluate it through the governance layer."
    )

    if st.button(
        "🤖 GENERATE AI RESPONSE",
        use_container_width=True
    ):

        if not user_query.strip():

            st.warning(
                "Please enter a User Query first."
            )

            st.stop()

        try:

            # ---------------------------------
            # CLEAR OLD ANALYSIS
            # ---------------------------------

            st.session_state.analysis_result = None

            st.session_state.generated_response = ""

            st.session_state.response_source = ""


            # ---------------------------------
            # GENERATE RESPONSE
            # ---------------------------------

            response_generator = ResponseGenerator()

            generated_result = response_generator.generate(
                user_query,
                application_context
            )


            # ---------------------------------
            # SUPPORT DICTIONARY RESULT
            # ---------------------------------

            if isinstance(
                generated_result,
                dict
            ):

                generated_response = generated_result.get(
                    "response",
                    generated_result.get(
                        "ai_response",
                        ""
                    )
                )

                generated_source = generated_result.get(
                    "source",
                    "SIMULATED AI MODEL"
                )

            else:

                generated_response = str(
                    generated_result
                )

                generated_source = (
                    "SIMULATED AI MODEL"
                )


            # ---------------------------------
            # STORE RESPONSE
            # ---------------------------------

            if generated_response:

                st.session_state.generated_response = str(
                    generated_response
                )

                st.session_state.response_source = str(
                    generated_source
                )

                st.success(
                    "AI response generated successfully."
                )

            else:

                st.session_state.generated_response = ""

                st.session_state.response_source = ""

                st.warning(
                    "The response generator did not "
                    "return a response."
                )


        except Exception as error:

            st.session_state.generated_response = ""

            st.session_state.response_source = ""

            st.error(
                f"Unable to generate AI response: {error}"
            )

            with st.expander(
                "🔍 View Generation Error Details"
            ):

                st.code(
                    traceback.format_exc()
                )


# =================================
# ENTER EXISTING RESPONSE
# =================================

else:

    st.info(
        "Enter an existing AI response and "
        "ControlPlane.ai will evaluate it."
    )


    existing_response = st.text_area(
        "AI Response",
        placeholder=(
            "Paste the AI response you want "
            "ControlPlane.ai to evaluate."
        ),
        height=150,
        key="existing_response",
        on_change=clear_previous_response
    )


    if existing_response.strip():

        st.session_state.generated_response = (
            existing_response
        )

        st.session_state.response_source = (
            "USER PROVIDED"
        )

    else:

        st.session_state.generated_response = ""

        st.session_state.response_source = ""


# =================================
# GENERATED AI RESPONSE
# =================================

st.header(
    "🤖 Generated AI Response"
)


if (
    user_query.strip()
    and st.session_state.generated_response.strip()
):

    st.info(
        st.session_state.generated_response
    )

    st.caption(
        "Response source: "
        + (
            st.session_state.response_source
            or "USER PROVIDED"
        )
    )

else:

    st.info(
        "Enter a user query and generate or "
        "provide an AI response."
    )


# =================================
# ANALYZE RESPONSE BUTTON
# =================================

st.divider()


if st.button(
    "🔍 ANALYZE RESPONSE",
    use_container_width=True
):

    # =================================
    # VALIDATION
    # =================================

    if not user_query.strip():

        st.warning(
            "Please enter a User Query first."
        )

        st.stop()


    ai_response = (
        st.session_state.generated_response.strip()
    )


    if not ai_response:

        st.warning(
            "Please generate or enter an AI response first."
        )

        st.stop()


    # =================================
    # START GOVERNANCE ANALYSIS
    # =================================

    with st.spinner(
        "ControlPlane.ai is evaluating the response..."
    ):

        try:

            # =================================
            # INITIALIZE ENGINES
            # =================================

            performance_engine = PerformanceEngine()

            responsible_engine = ResponsibleAIEngine()

            context_engine = ContextEngine()

            cost_engine = CostEngine()

            knowledge_engine = KnowledgeBase()

            policy_engine = PolicyEngine()

            risk_engine = RiskEngine()

            confidence_engine = ConfidenceEngine()

            decision_engine = DecisionEngine()


            # =================================
            # PERFORMANCE / HALLUCINATION
            # =================================

            try:

                performance_result = (
                    performance_engine.analyze(
                        user_query,
                        ai_response
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "PerformanceEngine failed: "
                    + str(error)
                ) from error


            # =================================
            # RESPONSIBLE AI
            # =================================

            try:

                responsible_result = (
                    responsible_engine.analyze(
                        ai_response
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "ResponsibleAIEngine failed: "
                    + str(error)
                ) from error


            # =================================
            # CONTEXT
            # =================================

            try:

                context_result = (
                    context_engine.analyze(
                        user_query,
                        application_context
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "ContextEngine failed: "
                    + str(error)
                ) from error


            # =================================
            # COST
            # =================================

            try:

                cost_result = (
                    cost_engine.analyze(
                        user_query,
                        ai_response
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "CostEngine failed: "
                    + str(error)
                ) from error


            # =================================
            # KNOWLEDGE GROUNDING
            # =================================

            try:

                knowledge_result = (
                    knowledge_engine.analyze(
                        user_query,
                        ai_response
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "KnowledgeBase failed: "
                    + str(error)
                ) from error


            # =================================
            # POLICY
            # =================================

            try:

                policy_result = (
                    policy_engine.analyze(
                        user_query,
                        ai_response,
                        application_context
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "PolicyEngine failed: "
                    + str(error)
                ) from error


            # =================================
            # VALIDATE ENGINE RESULTS
            # =================================

            engine_results = {

                "performance":
                    performance_result,

                "responsible":
                    responsible_result,

                "context":
                    context_result,

                "cost":
                    cost_result,

                "knowledge":
                    knowledge_result,

                "policy":
                    policy_result
            }


            for name, value in engine_results.items():

                if value is None:

                    raise ValueError(
                        f"{name} engine returned None."
                    )


                if not isinstance(
                    value,
                    dict
                ):

                    raise TypeError(
                        f"{name} engine returned "
                        f"{type(value).__name__} "
                        "instead of a dictionary."
                    )


            # =================================
            # RISK ENGINE
            # =================================

            try:

                risk_result = (
                    risk_engine.analyze(
                        performance_result,
                        responsible_result,
                        context_result,
                        cost_result,
                        knowledge_result,
                        policy_result
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "RiskEngine failed: "
                    + str(error)
                ) from error


            if not isinstance(
                risk_result,
                dict
            ):

                raise TypeError(
                    "RiskEngine did not return a dictionary."
                )


            # =================================
            # CONFIDENCE ENGINE
            # =================================

            try:

                confidence_result = (
                    confidence_engine.analyze(

                        performance_result.get(
                            "hallucination_risk"
                        ),

                        responsible_result.get(
                            "risk_level"
                        ),

                        context_result.get(
                            "context_risk"
                        ),

                        cost_result.get(
                            "cost_risk"
                        ),
                        knowledge_result.get(
                            "knowledge_risk"
                        ),

                        policy_result.get(
                             "policy_risk"
                        )
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "ConfidenceEngine failed: "
                    + str(error)
                ) from error


            if not isinstance(
                confidence_result,
                dict
            ):

                raise TypeError(
                    "ConfidenceEngine did not "
                    "return a dictionary."
                )


            # =================================
            # DECISION ENGINE
            # =================================

            try:

                decision_result = (
                    decision_engine.decide(
                        risk_result,
                        policy_result
                    )
                )

            except Exception as error:

                raise RuntimeError(
                    "DecisionEngine failed: "
                    + str(error)
                ) from error


            if not isinstance(
                decision_result,
                dict
            ):

                raise TypeError(
                    "DecisionEngine did not "
                    "return a dictionary."
                )


            # =================================
            # SAVE COMPLETE ANALYSIS
            # =================================

            save_analysis(

                user_query=user_query,

                ai_response=ai_response,

                application_context=application_context,

                hallucination_risk=(
                    performance_result.get(
                        "hallucination_risk",
                        "UNKNOWN"
                    )
                ),

                responsible_ai_risk=(
                    responsible_result.get(
                        "risk_level",
                        "UNKNOWN"
                    )
                ),

                context_risk=(
                    context_result.get(
                        "context_risk",
                        "UNKNOWN"
                    )
                ),

                cost_risk=(
                    cost_result.get(
                        "cost_risk",
                        "UNKNOWN"
                    )
                ),

                knowledge_risk=(
                    knowledge_result.get(
                        "knowledge_risk",
                        "UNKNOWN"
                    )
                ),

                knowledge_status=(
                    knowledge_result.get(
                        "knowledge_status",
                        "UNKNOWN"
                    )
                ),

                policy_risk=(
                    policy_result.get(
                        "policy_risk",
                        "UNKNOWN"
                    )
                ),

                policy_status=(
                    policy_result.get(
                        "policy_status",
                        "UNKNOWN"
                    )
                ),

                confidence_score=(
                    confidence_result.get(
                        "confidence_score",
                        0
                    )
                ),

                confidence_level=(
                    confidence_result.get(
                        "confidence_level",
                        "UNKNOWN"
                    )
                ),

                total_risk_score=(
                    risk_result.get(
                        "total_risk_score",
                        0
                    )
                ),

                overall_risk=(
                    decision_result.get(
                        "overall_risk",
                        risk_result.get(
                            "overall_risk",
                            "UNKNOWN"
                        )
                    )
                ),

                decision=(
                    decision_result.get(
                        "decision",
                        "UNKNOWN"
                    )
                ),

                reason=(
                    decision_result.get(
                        "reason",
                        "No reason provided."
                    )
                )
            )


            # =================================
            # STORE RESULT
            # =================================

            st.session_state.analysis_result = {

                "performance":
                    performance_result,

                "responsible":
                    responsible_result,

                "context":
                    context_result,

                "cost":
                    cost_result,

                "knowledge":
                    knowledge_result,

                "policy":
                    policy_result,

                "risk":
                    risk_result,

                "confidence":
                    confidence_result,

                "decision":
                    decision_result,

                "ai_response":
                    ai_response,

                "user_query":
                    user_query,

                "application_context":
                    application_context
            }


            st.success(
                "Analysis completed and saved to "
                "the ControlPlane.ai audit database."
            )


        except Exception as error:

            st.session_state.analysis_result = None

            st.error(
                f"Analysis failed: {error}"
            )

            # ---------------------------------
            # IMPORTANT DEBUG INFORMATION
            # ---------------------------------

            with st.expander(
                "🔍 View Detailed Error / Traceback"
            ):

                st.code(
                    traceback.format_exc()
                )

            st.stop()


# =================================
# DISPLAY GOVERNANCE RESULT
# =================================

result = st.session_state.analysis_result


if result:

    performance_result = result["performance"]

    responsible_result = result["responsible"]

    context_result = result["context"]

    cost_result = result["cost"]

    knowledge_result = result["knowledge"]

    policy_result = result["policy"]

    risk_result = result["risk"]

    confidence_result = result["confidence"]

    decision_result = result["decision"]


    # =================================
    # GOVERNANCE RESULT
    # =================================

    st.divider()

    st.title(
        "🛡️ ControlPlane.ai Governance Result"
    )


    # =================================
    # AI RESPONSE
    # =================================

    st.header(
        "🤖 AI Response"
    )

    st.info(
        result["ai_response"]
    )


    # =================================
    # CONFIDENCE
    # =================================

    st.header(
        "🎯 AI Confidence"
    )


    confidence_col1, confidence_col2 = st.columns(2)


    with confidence_col1:

        st.metric(
            "Confidence Score",
            f"{confidence_result.get('confidence_score', 0)}%"
        )


    with confidence_col2:

        st.metric(
            "Confidence Level",
            confidence_result.get(
                "confidence_level",
                "UNKNOWN"
            )
        )


    try:

        confidence_value = int(
            confidence_result.get(
                "confidence_score",
                0
            )
        )

    except:

        confidence_value = 0


    st.progress(
        max(
            0,
            min(
                confidence_value,
                100
            )
        )
    )


    # =================================
    # GOVERNANCE RISK
    # =================================

    st.header(
        "⚠️ Governance Risk Analysis"
    )


    risk_col1, risk_col2, risk_col3 = st.columns(3)


    with risk_col1:

        st.metric(
            "Hallucination Risk",
            performance_result.get(
                "hallucination_risk",
                "UNKNOWN"
            )
        )


    with risk_col2:

        st.metric(
            "Responsible AI Risk",
            responsible_result.get(
                "risk_level",
                "UNKNOWN"
            )
        )


    with risk_col3:

        st.metric(
            "Context Risk",
            context_result.get(
                "context_risk",
                "UNKNOWN"
            )
        )


    risk_col4, risk_col5, risk_col6 = st.columns(3)


    with risk_col4:

        st.metric(
            "Cost Risk",
            cost_result.get(
                "cost_risk",
                "UNKNOWN"
            )
        )


    with risk_col5:

        st.metric(
            "Knowledge Risk",
            knowledge_result.get(
                "knowledge_risk",
                "UNKNOWN"
            )
        )


    with risk_col6:

        st.metric(
            "Policy Risk",
            policy_result.get(
                "policy_risk",
                "UNKNOWN"
            )
        )


    # =================================
    # GOVERNANCE CHECKS
    # =================================

    st.divider()

    st.header(
        "🔎 Governance Checks"
    )


    check_col1, check_col2 = st.columns(2)


    with check_col1:

        st.metric(
            "Knowledge Status",
            knowledge_result.get(
                "knowledge_status",
                "UNKNOWN"
            )
        )


    with check_col2:

        st.metric(
            "Policy Status",
            policy_result.get(
                "policy_status",
                "UNKNOWN"
            )
        )


    # =================================
    # RISK SCORE
    # =================================

    st.divider()


    score_col1, score_col2 = st.columns(2)


    with score_col1:

        st.metric(
            "Total Risk Score",
            risk_result.get(
                "total_risk_score",
                0
            )
        )


    with score_col2:

        st.metric(
            "Overall Risk",
            decision_result.get(
                "overall_risk",
                "UNKNOWN"
            )
        )


    # =================================
    # FINAL DECISION
    # =================================

    st.divider()

    st.header(
        "🚦 Final Governance Decision"
    )


    decision = decision_result.get(
        "decision",
        "UNKNOWN"
    )


    if decision == "ALLOW":

        st.success(
            f"🟢 Decision: {decision}"
        )


    elif decision == "WARN":

        st.warning(
            f"🟡 Decision: {decision}"
        )


    elif decision == "HUMAN REVIEW":

        st.warning(
            f"🟠 Decision: {decision}"
        )

        st.info(
            "👤 This response has been escalated "
            "to Human Review because automated "
            "governance checks detected significant risk."
        )


    else:

        st.error(
            f"🔴 Decision: {decision}"
        )


    st.write(
        f"**Reason:** "
        f"{decision_result.get('reason', 'No reason provided.')}"
    )


    # =================================
    # POLICY VIOLATIONS
    # =================================

    violations = policy_result.get(
        "violations",
        []
    )


    if violations:

        st.divider()

        st.header(
            "⚠️ Policy Violations Detected"
        )


        for violation in violations:

            st.warning(
                str(violation)
            )

    else:

        st.success(
            "✅ No policy violations detected."
        )


    # =================================
    # AUDIT CONFIRMATION
    # =================================

    st.success(
        "✅ Analysis saved to ControlPlane.ai audit database."
    )


    # =================================
    # DETAILED ANALYSIS
    # =================================

    with st.expander(
        "🔍 View Detailed Analysis"
    ):

        st.write(
            "### User Query"
        )

        st.write(
            result["user_query"]
        )


        st.write(
            "### Application Context"
        )

        st.write(
            result["application_context"]
        )


        st.write(
            "### Hallucination Analysis"
        )

        st.json(
            performance_result
        )


        st.write(
            "### Responsible AI Analysis"
        )

        st.json(
            responsible_result
        )


        st.write(
            "### Context Analysis"
        )

        st.json(
            context_result
        )


        st.write(
            "### Cost Analysis"
        )

        st.json(
            cost_result
        )


        st.write(
            "### Knowledge Analysis"
        )

        st.json(
            knowledge_result
        )


        st.write(
            "### Policy Analysis"
        )

        st.json(
            policy_result
        )


        st.write(
            "### Risk Analysis"
        )

        st.json(
            risk_result
        )


        st.write(
            "### Confidence Analysis"
        )

        st.json(
            confidence_result
        )


        st.write(
            "### Decision Analysis"
        )

        st.json(
            decision_result
        )