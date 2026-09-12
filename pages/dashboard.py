import streamlit as st
import pandas as pd

from pages.shared_ui import apply_theme, sidebar

from database.db import get_all_logs


# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="ControlPlane.ai Dashboard",
    page_icon="📊",
    layout="wide"
)

apply_theme()
sidebar("dashboard")


# ---------------------------------
# PAGE TITLE
# ---------------------------------

# ---------------------------------
# PAGE HEADER
# ---------------------------------

st.markdown(
"""<div class="cp-page-header" style="padding-top: 28px;">

<div class="cp-page-kicker">
📊 &nbsp; GOVERNANCE INTELLIGENCE CENTER
</div>

<div class="cp-page-title">
ControlPlane<span class="accent">.ai</span> Dashboard
</div>

<div class="cp-page-description">
Monitor AI response decisions, risk levels,
knowledge grounding, policy compliance,
confidence and governance activity.
</div>

</div>""",
unsafe_allow_html=True,
)


# ---------------------------------
# GET DATA
# ---------------------------------

logs = get_all_logs()


# ---------------------------------
# NO DATA
# ---------------------------------

if not logs:

    st.info(
        "No AI analyses available yet. "
        "Go to the Simulator and analyze an AI response."
    )


else:

    # ---------------------------------
    # CREATE DATAFRAME
    # COLUMN ORDER MUST MATCH db.py
    # ---------------------------------

    df = pd.DataFrame(
        logs,
        columns=[
            "ID",
            "User Query",
            "AI Response",
            "Application Context",
            "Hallucination Risk",
            "Responsible AI Risk",
            "Context Risk",
            "Cost Risk",
            "Knowledge Risk",
            "Knowledge Status",
            "Policy Risk",
            "Policy Status",
            "Confidence Score",
            "Confidence Level",
            "Total Risk Score",
            "Overall Risk",
            "Decision",
            "Reason",
            "Created At"
        ]
    )


    # ---------------------------------
    # CONVERT CONFIDENCE TO NUMERIC
    # ---------------------------------

    df["Confidence Score"] = pd.to_numeric(
        df["Confidence Score"],
        errors="coerce"
    )


    # ---------------------------------
    # TOP METRICS
    # ---------------------------------

    total_analyses = len(df)

    allowed = len(
        df[df["Decision"] == "ALLOW"]
    )

    blocked = len(
        df[df["Decision"] == "BLOCK"]
    )

    human_review = len(
        df[df["Decision"] == "HUMAN REVIEW"]
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Analyses",
            total_analyses
        )


    with col2:

        st.metric(
            "Allowed",
            allowed
        )


    with col3:

        st.metric(
            "Blocked",
            blocked
        )


    with col4:

        st.metric(
            "Human Review",
            human_review
        )


    # ---------------------------------
    # AVERAGE CONFIDENCE
    # ---------------------------------

    st.divider()

    st.subheader("AI Confidence Overview")


    average_confidence = df[
        "Confidence Score"
    ].mean()


    if pd.notna(average_confidence):

        average_confidence = round(
            average_confidence,
            1
        )

    else:

        average_confidence = 0


    confidence_counts = (
        df["Confidence Level"]
        .dropna()
        .value_counts()
    )


    if not confidence_counts.empty:

        most_common_confidence = (
            confidence_counts.index[0]
        )

    else:

        most_common_confidence = "N/A"


    confidence_col1, confidence_col2 = st.columns(2)


    with confidence_col1:

        st.metric(
            "Average Confidence Score",
            f"{average_confidence}%"
        )


    with confidence_col2:

        st.metric(
            "Most Common Confidence",
            most_common_confidence
        )


    # ---------------------------------
    # GOVERNANCE OVERVIEW
    # ---------------------------------

    st.divider()

    st.subheader("Governance Overview")


    governance_col1, governance_col2 = st.columns(2)


    knowledge_grounded = len(
        df[
            df["Knowledge Status"] == "GROUNDED"
        ]
    )


    policy_violations = len(
        df[
            df["Policy Status"] == "VIOLATION"
        ]
    )


    with governance_col1:

        st.metric(
            "Knowledge Grounded Responses",
            knowledge_grounded
        )


    with governance_col2:

        st.metric(
            "Policy Violations",
            policy_violations
        )


    # ---------------------------------
    # RISK DISTRIBUTION
    # ---------------------------------

    st.divider()

    st.subheader("Risk Distribution")


    risk_counts = (
        df["Overall Risk"]
        .value_counts()
    )


    st.bar_chart(
        risk_counts
    )


    # ---------------------------------
    # DECISION DISTRIBUTION
    # ---------------------------------

    st.divider()

    st.subheader("Decision Distribution")


    decision_counts = (
        df["Decision"]
        .value_counts()
    )


    st.bar_chart(
        decision_counts
    )


    # ---------------------------------
    # CONFIDENCE DISTRIBUTION
    # ---------------------------------

    st.divider()

    st.subheader("Confidence Distribution")


    confidence_distribution = (
        df["Confidence Level"]
        .value_counts()
    )


    st.bar_chart(
        confidence_distribution
    )


    # ---------------------------------
    # POLICY DISTRIBUTION
    # ---------------------------------

    st.divider()

    st.subheader("Policy Compliance Distribution")


    policy_distribution = (
        df["Policy Status"]
        .value_counts()
    )


    st.bar_chart(
        policy_distribution
    )


    # ---------------------------------
    # KNOWLEDGE DISTRIBUTION
    # ---------------------------------

    st.divider()

    st.subheader("Knowledge Grounding Distribution")


    knowledge_distribution = (
        df["Knowledge Status"]
        .value_counts()
    )


    st.bar_chart(
        knowledge_distribution
    )


    # ---------------------------------
    # RECENT ANALYSES
    # ---------------------------------

    st.divider()

    st.subheader("Recent AI Analyses")


    display_df = df[
        [
            "ID",
            "User Query",
            "Application Context",
            "Knowledge Status",
            "Policy Status",
            "Overall Risk",
            "Confidence Score",
            "Confidence Level",
            "Decision",
            "Created At"
        ]
    ]


    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


    # ---------------------------------
    # DETAILED ANALYSIS
    # ---------------------------------

    st.divider()

    st.subheader("Detailed Analysis")


    for _, row in df.iterrows():

        with st.expander(
            f"Analysis #{row['ID']} — "
            f"{row['Decision']} — "
            f"{row['Overall Risk']} Risk"
        ):


            # -----------------------------
            # USER QUERY
            # -----------------------------

            st.write("### User Query")

            st.info(
                row["User Query"]
            )


            # -----------------------------
            # AI RESPONSE
            # -----------------------------

            st.write("### AI Response")

            st.write(
                row["AI Response"]
            )


            # -----------------------------
            # RISK ANALYSIS
            # -----------------------------

            st.divider()

            st.write("### Risk Analysis")


            risk_col1, risk_col2, risk_col3 = st.columns(3)


            with risk_col1:

                st.metric(
                    "Hallucination Risk",
                    row["Hallucination Risk"]
                )


            with risk_col2:

                st.metric(
                    "Responsible AI Risk",
                    row["Responsible AI Risk"]
                )


            with risk_col3:

                st.metric(
                    "Context Risk",
                    row["Context Risk"]
                )


            risk_col4, risk_col5, risk_col6 = st.columns(3)


            with risk_col4:

                st.metric(
                    "Cost Risk",
                    row["Cost Risk"]
                )


            with risk_col5:

                st.metric(
                    "Knowledge Risk",
                    row["Knowledge Risk"]
                )


            with risk_col6:

                st.metric(
                    "Policy Risk",
                    row["Policy Risk"]
                )


            # -----------------------------
            # GOVERNANCE CHECKS
            # -----------------------------

            st.divider()

            st.write("### Governance Checks")


            status_col1, status_col2 = st.columns(2)


            with status_col1:

                st.metric(
                    "Knowledge Status",
                    row["Knowledge Status"]
                )


            with status_col2:

                st.metric(
                    "Policy Status",
                    row["Policy Status"]
                )


            # -----------------------------
            # CONFIDENCE ANALYSIS
            # -----------------------------

            st.divider()

            st.write("### Confidence Analysis")


            confidence_col1, confidence_col2 = st.columns(2)


            confidence_score = row[
                "Confidence Score"
            ]


            with confidence_col1:

                if pd.notna(confidence_score):

                    st.metric(
                        "Confidence Score",
                        f"{round(confidence_score, 1)}%"
                    )

                else:

                    st.metric(
                        "Confidence Score",
                        "N/A"
                    )


            with confidence_col2:

                st.metric(
                    "Confidence Level",
                    row["Confidence Level"]
                )


            if pd.notna(confidence_score):

                progress_value = max(
                    0,
                    min(
                        int(confidence_score),
                        100
                    )
                )

                st.progress(
                    progress_value
                )


            # -----------------------------
            # FINAL DECISION
            # -----------------------------

            st.divider()

            st.write(
                "### Final Governance Decision"
            )


            result1, result2, result3 = st.columns(3)


            with result1:

                st.metric(
                    "Total Risk Score",
                    row["Total Risk Score"]
                )


            with result2:

                st.metric(
                    "Overall Risk",
                    row["Overall Risk"]
                )


            with result3:

                st.metric(
                    "Decision",
                    row["Decision"]
                )


            # -----------------------------
            # REASON
            # -----------------------------

            st.write("### Decision Reason")

            st.warning(
                row["Reason"]
            )


            # -----------------------------
            # DATE
            # -----------------------------

            st.caption(
                f"Analyzed on: {row['Created At']}"
            )