import streamlit as st
import pandas as pd

from pages.shared_ui import apply_theme, sidebar

from database.db import (
    get_human_review_logs,
    update_human_decision,
)

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="ControlPlane.ai Human Review",
    page_icon="👤",
    layout="wide"
)

# ============================================================
# SHARED CONTROLPLANE.AI UI
# ============================================================

apply_theme()
sidebar("review")
# ---------------------------------
# PAGE TITLE
# ---------------------------------

st.markdown(
"""<div class="cp-page-header" style="padding-top: 28px;">

<div class="cp-page-kicker">
👤 &nbsp; HUMAN-IN-THE-LOOP GOVERNANCE
</div>

<div class="cp-page-title">
ControlPlane<span class="accent">.ai</span> Human Review
</div>

<div class="cp-page-description">
Review high-risk AI responses that require
human governance approval before release.
</div>

</div>""",
unsafe_allow_html=True,
)


# ---------------------------------
# GET HUMAN REVIEW LOGS
# ---------------------------------

logs = get_human_review_logs()


# ---------------------------------
# NO HUMAN REVIEW CASES
# ---------------------------------

if not logs:

    st.success(
        "🎉 No AI responses are currently waiting for human review."
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
    # TOP METRICS
    # ---------------------------------

    total_reviews = len(df)

    high_risk = len(
        df[
            df["Overall Risk"] == "HIGH"
        ]
    )

    critical_risk = len(
        df[
            df["Overall Risk"] == "CRITICAL"
        ]
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Pending Reviews",
            total_reviews
        )


    with col2:

        st.metric(
            "High Risk Cases",
            high_risk
        )


    with col3:

        st.metric(
            "Critical Risk Cases",
            critical_risk
        )


    st.divider()


    # ---------------------------------
    # HUMAN REVIEW CASES
    # ---------------------------------

    st.subheader("Pending Review Cases")


    for _, row in df.iterrows():

        with st.expander(
            f"Review Case #{row['ID']} — "
            f"{row['Overall Risk']} Risk"
        ):


            # ---------------------------------
            # BASIC INFORMATION
            # ---------------------------------

            st.write("### Analysis Information")


            info_col1, info_col2, info_col3 = st.columns(3)


            with info_col1:

                st.metric(
                    "Application Context",
                    row["Application Context"]
                )


            with info_col2:

                st.metric(
                    "Overall Risk",
                    row["Overall Risk"]
                )


            with info_col3:

                st.metric(
                    "Created At",
                    row["Created At"]
                )


            # ---------------------------------
            # USER QUERY
            # ---------------------------------

            st.divider()

            st.write("### User Query")

            st.info(
                row["User Query"]
            )


            # ---------------------------------
            # AI RESPONSE
            # ---------------------------------

            st.write("### AI Response")

            st.write(
                row["AI Response"]
            )


            # ---------------------------------
            # RISK ANALYSIS
            # ---------------------------------

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


            # ---------------------------------
            # GOVERNANCE CHECKS
            # ---------------------------------

            st.divider()

            st.write("### Governance Checks")


            check_col1, check_col2 = st.columns(2)


            with check_col1:

                st.metric(
                    "Knowledge Status",
                    row["Knowledge Status"]
                )


            with check_col2:

                st.metric(
                    "Policy Status",
                    row["Policy Status"]
                )


            # ---------------------------------
            # CONFIDENCE ANALYSIS
            # ---------------------------------

            st.divider()

            st.write("### Confidence Analysis")


            confidence_col1, confidence_col2 = st.columns(2)


            confidence_score = pd.to_numeric(
                row["Confidence Score"],
                errors="coerce"
            )


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


            # ---------------------------------
            # AUTOMATED DECISION
            # ---------------------------------

            st.divider()

            st.write("### Automated Governance Decision")


            decision_col1, decision_col2 = st.columns(2)


            with decision_col1:

                st.metric(
                    "Risk Score",
                    row["Total Risk Score"]
                )


            with decision_col2:

                st.metric(
                    "Current Decision",
                    row["Decision"]
                )


            st.write("### System Reason")

            st.warning(
                row["Reason"]
            )


            # ---------------------------------
            # HUMAN DECISION
            # ---------------------------------

            st.divider()

            st.write("### Human Reviewer Decision")

            st.write(
                "Review the complete analysis and make the final decision."
            )


            action_col1, action_col2 = st.columns(2)


            with action_col1:

                if st.button(
                    "✅ APPROVE RESPONSE",
                    key=f"approve_{row['ID']}"
                ):

                    update_human_decision(
                        row["ID"],
                        "ALLOW"
                    )

                    st.success(
                        "Response approved by human reviewer."
                    )

                    st.rerun()


            with action_col2:

                if st.button(
                    "🚫 BLOCK RESPONSE",
                    key=f"block_{row['ID']}"
                ):

                    update_human_decision(
                        row["ID"],
                        "BLOCK"
                    )

                    st.error(
                        "Response blocked by human reviewer."
                    )

                    st.rerun()