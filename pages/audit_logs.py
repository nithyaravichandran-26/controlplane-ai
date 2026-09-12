import streamlit as st
import pandas as pd

from pages.shared_ui import apply_theme, sidebar
from database.db import get_all_logs


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ControlPlane.ai Audit Logs",
    page_icon="📋",
    layout="wide",
)


# ============================================================
# SHARED CONTROLPLANE.AI UI
# ============================================================

apply_theme()
sidebar("audit_logs")


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
"""<div class="cp-page-header" style="padding-top: 28px;">

<div class="cp-page-kicker">
🛡️ &nbsp; GOVERNANCE AUDIT CENTER
</div>

<div class="cp-page-title">
ControlPlane<span class="accent">.ai</span>
<span style="font-size:0.55em; color:#8ea6bd;">
Audit Logs
</span>
</div>

<div class="cp-page-description">
Complete governance history of AI responses,
risk assessments, policy checks, confidence scores
and final governance decisions.
</div>

</div>""",
unsafe_allow_html=True,
)


# ============================================================
# DATABASE
# ============================================================

logs = get_all_logs()


# ============================================================
# NO LOGS
# ============================================================

if not logs:

    st.markdown(
        """
        <div style="
            padding: 35px;
            border-radius: 16px;
            border: 1px solid rgba(39,137,224,0.30);
            background: linear-gradient(
                145deg,
                rgba(5,32,54,0.90),
                rgba(2,17,30,0.96)
            );
            text-align: center;
            margin-top: 20px;
        ">
            <div style="
                font-size: 2rem;
                margin-bottom: 10px;
            ">
                📋
            </div>

            <div style="
                color:#eef7ff;
                font-size:1.1rem;
                font-weight:800;
            ">
                No Audit Logs Available
            </div>

            <div style="
                color:#8197ad;
                margin-top:8px;
            ">
                Go to the Live Simulator and analyze
                an AI response to create an audit record.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    # ========================================================
    # DATAFRAME
    # ========================================================

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
            "Created At",
        ],
    )


    # ========================================================
    # TOP METRICS
    # ========================================================

    total_logs = len(df)

    allowed = len(
        df[df["Decision"] == "ALLOW"]
    )

    blocked = len(
        df[df["Decision"] == "BLOCK"]
    )

    human_review = len(
        df[
            df["Decision"].isin(
                ["HUMAN REVIEW", "REVIEW"]
            )
        ]
    )


    st.markdown(
        """
        <div style="
            margin-top: 8px;
            margin-bottom: 12px;
            color:#eef7ff;
            font-size:1.15rem;
            font-weight:850;
        ">
            📊 Platform at a Glance
        </div>

        <div style="
            color:#7189a0;
            font-size:0.75rem;
            margin-bottom:18px;
        ">
            Real-time overview of governance activity
        </div>
        """,
        unsafe_allow_html=True,
    )


    metric1, metric2, metric3, metric4 = st.columns(
        4,
        gap="medium"
    )


    with metric1:

        st.metric(
            "Total Analyses",
            total_logs,
        )


    with metric2:

        st.metric(
            "Allowed",
            allowed,
        )


    with metric3:

        st.metric(
            "Blocked",
            blocked,
        )


    with metric4:

        st.metric(
            "Human Review",
            human_review,
        )


    # ========================================================
    # SPACE
    # ========================================================

    st.markdown(
        "<div style='height:18px'></div>",
        unsafe_allow_html=True,
    )


    # ========================================================
    # FILTER SECTION
    # ========================================================

    st.markdown(
        """
        <div style="
            margin-bottom:15px;
            color:#f1f7ff;
            font-size:1.15rem;
            font-weight:850;
        ">
            🔎 Filter Audit Logs
        </div>
        """,
        unsafe_allow_html=True,
    )


    filter1, filter2, filter3, filter4 = st.columns(
        4,
        gap="medium"
    )


    with filter1:

        decision_filter = st.selectbox(
            "Decision",
            [
                "ALL",
                "ALLOW",
                "WARN",
                "HUMAN REVIEW",
                "REVIEW",
                "BLOCK",
            ],
        )


    with filter2:

        risk_filter = st.selectbox(
            "Overall Risk",
            [
                "ALL",
                "LOW",
                "MEDIUM",
                "HIGH",
                "CRITICAL",
            ],
        )


    with filter3:

        confidence_filter = st.selectbox(
            "Confidence",
            [
                "ALL",
                "HIGH",
                "MEDIUM",
                "LOW",
            ],
        )


    with filter4:

        policy_filter = st.selectbox(
            "Policy Status",
            [
                "ALL",
                "COMPLIANT",
                "WARNING",
                "VIOLATION",
            ],
        )


    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_df = df.copy()


    if decision_filter != "ALL":

        if decision_filter == "HUMAN REVIEW":

            filtered_df = filtered_df[
                filtered_df["Decision"].isin(
                    ["HUMAN REVIEW", "REVIEW"]
                )
            ]

        else:

            filtered_df = filtered_df[
                filtered_df["Decision"]
                == decision_filter
            ]


    if risk_filter != "ALL":

        filtered_df = filtered_df[
            filtered_df["Overall Risk"]
            == risk_filter
        ]


    if confidence_filter != "ALL":

        filtered_df = filtered_df[
            filtered_df["Confidence Level"]
            == confidence_filter
        ]


    if policy_filter != "ALL":

        filtered_df = filtered_df[
            filtered_df["Policy Status"]
            == policy_filter
        ]


    # ========================================================
    # EMPTY FILTER RESULT
    # ========================================================

    if filtered_df.empty:

        st.warning(
            "No audit logs match the selected filters."
        )

    else:

        # ====================================================
        # AUDIT RECORDS
        # ====================================================

        st.markdown(
            """
            <div style="
                margin-top:20px;
                margin-bottom:14px;
                color:#f1f7ff;
                font-size:1.15rem;
                font-weight:850;
            ">
                📋 Audit Records
            </div>
            """,
            unsafe_allow_html=True,
        )


        display_df = filtered_df[
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
                "Created At",
            ]
        ]


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
        )


        # ====================================================
        # DETAILED RECORDS
        # ====================================================

        st.markdown(
            """
            <div style="
                margin-top:28px;
                margin-bottom:14px;
                color:#f1f7ff;
                font-size:1.15rem;
                font-weight:850;
            ">
                🔍 Detailed Audit Records
            </div>
            """,
            unsafe_allow_html=True,
        )


        for _, row in filtered_df.iterrows():

            with st.expander(
                f"Analysis #{row['ID']}  •  "
                f"{row['Decision']}  •  "
                f"{row['Overall Risk']} Risk"
            ):

                # --------------------------------------------
                # BASIC INFORMATION
                # --------------------------------------------

                info1, info2, info3 = st.columns(3)


                with info1:

                    st.write(
                        "**Application Context**"
                    )

                    st.write(
                        row["Application Context"]
                    )


                with info2:

                    st.write(
                        "**Created At**"
                    )

                    st.write(
                        row["Created At"]
                    )


                with info3:

                    st.write(
                        "**Final Decision**"
                    )

                    st.write(
                        row["Decision"]
                    )


                st.divider()


                # --------------------------------------------
                # USER QUERY
                # --------------------------------------------

                st.write("### User Query")

                st.info(
                    row["User Query"]
                )


                # --------------------------------------------
                # AI RESPONSE
                # --------------------------------------------

                st.write("### AI Response")

                st.write(
                    row["AI Response"]
                )


                st.divider()


                # --------------------------------------------
                # RISK ANALYSIS
                # --------------------------------------------

                st.write("### Risk Analysis")


                risk1, risk2, risk3 = st.columns(3)


                with risk1:

                    st.metric(
                        "Hallucination Risk",
                        row["Hallucination Risk"],
                    )


                with risk2:

                    st.metric(
                        "Responsible AI Risk",
                        row["Responsible AI Risk"],
                    )


                with risk3:

                    st.metric(
                        "Context Risk",
                        row["Context Risk"],
                    )


                risk4, risk5, risk6 = st.columns(3)


                with risk4:

                    st.metric(
                        "Cost Risk",
                        row["Cost Risk"],
                    )


                with risk5:

                    st.metric(
                        "Knowledge Risk",
                        row["Knowledge Risk"],
                    )


                with risk6:

                    st.metric(
                        "Policy Risk",
                        row["Policy Risk"],
                    )


                st.divider()


                # --------------------------------------------
                # GOVERNANCE CHECKS
                # --------------------------------------------

                st.write(
                    "### Governance Checks"
                )


                check1, check2 = st.columns(2)


                with check1:

                    st.metric(
                        "Knowledge Status",
                        row["Knowledge Status"],
                    )


                with check2:

                    st.metric(
                        "Policy Status",
                        row["Policy Status"],
                    )


                st.divider()


                # --------------------------------------------
                # CONFIDENCE
                # --------------------------------------------

                st.write(
                    "### Confidence Analysis"
                )


                confidence_score = pd.to_numeric(
                    row["Confidence Score"],
                    errors="coerce",
                )


                confidence1, confidence2 = st.columns(2)


                with confidence1:

                    if pd.notna(confidence_score):

                        st.metric(
                            "Confidence Score",
                            f"{round(confidence_score, 1)}%",
                        )

                    else:

                        st.metric(
                            "Confidence Score",
                            "N/A",
                        )


                with confidence2:

                    st.metric(
                        "Confidence Level",
                        row["Confidence Level"],
                    )


                if pd.notna(confidence_score):

                    progress_value = max(
                        0,
                        min(
                            int(confidence_score),
                            100,
                        ),
                    )

                    st.progress(
                        progress_value
                    )


                st.divider()


                # --------------------------------------------
                # FINAL GOVERNANCE RESULT
                # --------------------------------------------

                st.write(
                    "### Governance Result"
                )


                result1, result2, result3 = st.columns(3)


                with result1:

                    st.metric(
                        "Total Risk Score",
                        row["Total Risk Score"],
                    )


                with result2:

                    st.metric(
                        "Overall Risk",
                        row["Overall Risk"],
                    )


                with result3:

                    st.metric(
                        "Decision",
                        row["Decision"],
                    )


                st.write(
                    "### Decision Reason"
                )

                st.warning(
                    row["Reason"]
                )