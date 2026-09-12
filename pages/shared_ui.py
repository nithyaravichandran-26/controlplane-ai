import streamlit as st


# ============================================================
# CONTROLPLANE.AI SHARED THEME
# ============================================================

def apply_theme():

    st.markdown(
        """
        <style>

        /* ======================================================
           GLOBAL
           ====================================================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 80% 0%,
                    rgba(0, 105, 210, 0.12),
                    transparent 28%
                ),
                linear-gradient(
                    180deg,
                    #020914 0%,
                    #020b15 100%
                );

            color: #eef5ff;
        }

        .block-container {
            max-width: 1500px !important;
            padding: 34px 28px 60px !important;
        }


        /* ======================================================
           HIDE DEFAULT STREAMLIT PAGE NAVIGATION
           ====================================================== */

        [data-testid="stSidebarNav"] {
            display: none !important;
        }


        /* ======================================================
           SIDEBAR
           ====================================================== */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #061321 0%,
                    #020b15 100%
                ) !important;

            border-right:
                1px solid rgba(39, 137, 224, 0.25) !important;
        }

        [data-testid="stSidebar"] > div:first-child {
            padding-top: 18px !important;
        }

        [data-testid="stSidebar"] .block-container {
            padding: 0 14px 20px !important;
        }


        /* ======================================================
           SIDEBAR BRAND
           ====================================================== */

        .cp-sidebar-brand {
            width: 100%;
            padding: 8px 0 24px;
        }

        .cp-sidebar-brand-row {
            width: 100%;

            display: flex;
            flex-direction: column;

            align-items: center;
            justify-content: center;

            text-align: center;
        }

        .cp-sidebar-shield {
            position: relative;

            width: 68px;
            height: 80px;

            display: flex;
            align-items: center;
            justify-content: center;

            margin: 0 auto 12px;

            box-sizing: border-box;

            color: #52c7ff;
            font-size: 38px;
            font-weight: 900;
            line-height: 1;

            background:
                linear-gradient(
                    145deg,
                    #1285d4 0%,
                    #0864aa 35%,
                    #073b6b 68%,
                    #052746 100%
                );

            clip-path: polygon(
                50% 0%,
                92% 13%,
                87% 59%,
                78% 78%,
                50% 100%,
                22% 78%,
                13% 59%,
                8% 13%
            );

            filter:
                drop-shadow(0 0 7px rgba(42, 183, 255, 0.85))
                drop-shadow(0 0 18px rgba(0, 132, 255, 0.40));

            text-shadow:
                0 0 5px rgba(82, 199, 255, 1),
                0 0 12px rgba(42, 183, 255, 0.95);

            z-index: 1;
        }

        .cp-sidebar-shield::before {
            content: "";

            position: absolute;
            left: 6px;
            top: 5px;
            right: 6px;
            bottom: 5px;

            background:
                linear-gradient(
                    145deg,
                    #0b5d9d 0%,
                    #064273 45%,
                    #032440 100%
                );

            clip-path: polygon(
                50% 0%,
                88% 13%,
                83% 59%,
                73% 77%,
                50% 100%,
                27% 77%,
                17% 59%,
                12% 13%
            );

            z-index: -1;
        }

        .cp-sidebar-brand-title {
            color: #f4f8ff;

            font-size: 1.08rem;
            font-weight: 850;

            line-height: 1.2;

            text-align: center;
        }

        .cp-sidebar-brand-sub {
            color: #8295aa;

            font-size: 0.70rem;

            margin-top: 5px;

            line-height: 1.3;

            text-align: center;
        }


        /* ======================================================
           NAVIGATION HEADING
           ====================================================== */

        .cp-nav-heading {
            color: #74879c;

            font-size: 0.65rem;
            font-weight: 850;

            letter-spacing: 0.13em;

            margin: 4px 4px 10px;
        }


        /* ======================================================
           NAVIGATION BUTTONS
           ====================================================== */

        [data-testid="stSidebar"] .stButton {
            width: 100% !important;

            margin: 0 !important;
            padding: 0 !important;
        }

        [data-testid="stSidebar"] .stButton > button {
            width: 100% !important;

            min-height: 43px !important;

            margin: 3px 0 !important;

            padding: 8px 14px !important;

            border-radius: 10px !important;

            border: 1px solid transparent !important;

            background: transparent !important;

            color: #dbe7f3 !important;

            font-size: 0.81rem !important;
            font-weight: 650 !important;

            text-align: left !important;

            box-shadow: none !important;

            transition:
                background 0.15s ease,
                border 0.15s ease,
                color 0.15s ease;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
            background:
                rgba(13, 102, 175, 0.18) !important;

            border:
                1px solid rgba(49, 158, 255, 0.25) !important;

            color: #ffffff !important;
        }


        /* ======================================================
           ACTIVE PAGE
           ====================================================== */

        [data-testid="stSidebar"]
        .cp-active-page
        + div
        .stButton > button {
            background:
                linear-gradient(
                    90deg,
                    #075cae,
                    #074b8c
                ) !important;

            border:
                1px solid rgba(49, 158, 255, 0.38) !important;

            color: #ffffff !important;

            box-shadow:
                inset 0 0 18px rgba(0, 132, 255, 0.08) !important;
        }


        /* ======================================================
           SIDEBAR DIVIDER
           ====================================================== */

        .cp-sidebar-divider {
            width: 100%;
            height: 1px;

            margin: 20px 0;

            background:
                rgba(97, 137, 175, 0.20);
        }


        /* ======================================================
           SYSTEM STATUS
           ====================================================== */

        .cp-status-row {
            width: 100%;

            display: flex;

            align-items: center;
            justify-content: space-between;

            box-sizing: border-box;

            padding: 7px 3px;

            color: #b9c8d8;

            font-size: 0.70rem;
        }

        .cp-status-left {
            display: flex;

            align-items: center;

            gap: 8px;
        }

        .cp-status-dot {
            width: 8px;
            height: 8px;

            flex: 0 0 8px;

            border-radius: 50%;

            background: #18df76;

            box-shadow:
                0 0 9px rgba(24, 223, 118, 0.55);
        }

        .cp-status-online {
            color: #18df76;

            font-weight: 800;
        }

        .cp-status-connected {
            color: #26a9ff;

            font-weight: 800;
        }


        /* ======================================================
           SIDEBAR ABOUT
           ====================================================== */

        .cp-sidebar-about {
            margin-top: 22px;

            padding: 14px;

            border-radius: 13px;

            border:
                1px solid rgba(39, 137, 224, 0.30);

            background:
                linear-gradient(
                    145deg,
                    rgba(6, 31, 53, 0.96),
                    rgba(2, 14, 25, 0.96)
                );
        }

        .cp-sidebar-about-title {
            color: #edf5ff;

            font-size: 0.78rem;

            font-weight: 850;

            margin-bottom: 7px;
        }

        .cp-sidebar-about-text {
            color: #7f93a8;

            font-size: 0.67rem;

            line-height: 1.55;
        }

        .cp-sidebar-footer {
            color: #53677c;

            text-align: center;

            font-size: 0.63rem;

            margin-top: 35px;

            padding-bottom: 8px;
        }


        /* ======================================================
           COMMON PAGE HEADER
           ====================================================== */

        .cp-page-header {
            margin-bottom: 30px;
        }

        .cp-page-kicker {
            display: inline-block;

            padding: 7px 14px;

            border-radius: 999px;

            border:
                1px solid rgba(49, 158, 255, 0.45);

            background:
                rgba(5, 63, 105, 0.35);

            color: #4ab6ff;

            font-size: 0.68rem;

            font-weight: 800;

            letter-spacing: 0.08em;
        }

        .cp-page-title {
            margin-top: 16px;

            color: #f5f9ff;

            font-size: 2.6rem;

            font-weight: 900;

            line-height: 1.1;
        }

        .cp-page-title .accent {
            color: #25a9ff;
        }

        .cp-page-description {
            margin-top: 12px;

            max-width: 850px;

            color: #91a4b8;

            font-size: 0.92rem;

            line-height: 1.6;
        }


        /* ======================================================
           METRICS
           ====================================================== */

        [data-testid="stMetric"] {
            background:
                linear-gradient(
                    145deg,
                    rgba(5, 28, 48, 0.95),
                    rgba(2, 15, 26, 0.95)
                );

            border:
                1px solid rgba(39, 137, 224, 0.28);

            border-radius: 14px;

            padding: 18px !important;
        }


        /* ======================================================
           BUTTONS
           ====================================================== */

        .stButton > button {
            border-radius: 10px !important;

            min-height: 42px !important;

            font-weight: 750 !important;
        }


        /* ======================================================
           EXPANDERS
           ====================================================== */

        [data-testid="stExpander"] {
            border:
                1px solid rgba(39, 137, 224, 0.28) !important;

            border-radius: 12px !important;

            background:
                rgba(3, 18, 31, 0.72) !important;
        }


        /* ======================================================
           DATAFRAME
           ====================================================== */

        [data-testid="stDataFrame"] {
            border-radius: 12px;

            overflow: hidden;
        }


        /* ======================================================
           MOBILE
           ====================================================== */

        @media (max-width: 900px) {

            .block-container {
                padding: 25px 16px 50px !important;
            }

            .cp-page-title {
                font-size: 2.1rem;
            }

            .cp-sidebar-shield {
                width: 60px;
                height: 72px;
            }
        }

        @media (max-width: 600px) {

            .cp-page-title {
                font-size: 1.8rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# NAVIGATION HELPER
# ============================================================

def _navigation_button(
    label,
    page_path,
    active=False,
    key=None
):

    if active:

        st.markdown(
            '<div class="cp-active-page"></div>',
            unsafe_allow_html=True
        )

    if st.button(
        label,
        key=key,
        use_container_width=True
    ):

        st.switch_page(page_path)


# ============================================================
# SHARED SIDEBAR
# ============================================================

def sidebar(active_page="overview"):

    with st.sidebar:

        # ====================================================
        # BRAND
        # ====================================================

        st.html(
            """
            <div class="cp-sidebar-brand">

                <div class="cp-sidebar-brand-row">

                    <div class="cp-sidebar-shield">
                        ✓
                    </div>

                    <div class="cp-sidebar-brand-title">
                        ControlPlane.ai
                    </div>

                    <div class="cp-sidebar-brand-sub">
                        AI Governance Platform
                    </div>

                </div>

            </div>
            """
        )


        # ====================================================
        # MAIN NAVIGATION
        # ====================================================

        st.html(
            """
            <div class="cp-nav-heading">
                MAIN NAVIGATION
            </div>
            """
        )


        # ----------------------------------------------------
        # OVERVIEW
        # ----------------------------------------------------

        _navigation_button(
            "🏠  Overview",
            "app.py",
            active=(active_page == "overview"),
            key="cp_nav_overview"
        )


        # ----------------------------------------------------
        # SIMULATOR
        # ----------------------------------------------------

        _navigation_button(
            "⚡  Live Simulator",
            "pages/simulator.py",
            active=(active_page == "simulator"),
            key="cp_nav_simulator"
        )


        # ----------------------------------------------------
        # DASHBOARD
        # ----------------------------------------------------

        _navigation_button(
            "📊  Risk Dashboard",
            "pages/dashboard.py",
            active=(active_page == "dashboard"),
            key="cp_nav_dashboard"
        )


        # ----------------------------------------------------
        # AUDIT LOGS
        # ----------------------------------------------------

        _navigation_button(
            "📋  Audit Logs",
            "pages/audit_logs.py",
            active=(active_page == "audit_logs"),
            key="cp_nav_audit_logs"
        )


        # ----------------------------------------------------
        # HUMAN REVIEW
        # ----------------------------------------------------

        _navigation_button(
            "👤  Human Review",
            "pages/human_review.py",
            active=(active_page == "human_review"),
            key="cp_nav_human_review"
        )


        # ====================================================
        # DIVIDER
        # ====================================================

        st.html(
            """
            <div class="cp-sidebar-divider"></div>
            """
        )


        # ====================================================
        # SYSTEM STATUS
        # ====================================================

        st.html(
            """
            <div class="cp-nav-heading">
                SYSTEM STATUS
            </div>
            """
        )


        # Risk Engine

        st.html(
            """
            <div class="cp-status-row">

                <div class="cp-status-left">

                    <span class="cp-status-dot"></span>

                    <span>
                        Risk Engine
                    </span>

                </div>

                <span class="cp-status-online">
                    Online
                </span>

            </div>
            """
        )


        # Policy Engine

        st.html(
            """
            <div class="cp-status-row">

                <div class="cp-status-left">

                    <span class="cp-status-dot"></span>

                    <span>
                        Policy Engine
                    </span>

                </div>

                <span class="cp-status-online">
                    Online
                </span>

            </div>
            """
        )


        # Knowledge Base

        st.html(
            """
            <div class="cp-status-row">

                <div class="cp-status-left">

                    <span class="cp-status-dot"></span>

                    <span>
                        Knowledge Base
                    </span>

                </div>

                <span class="cp-status-online">
                    Online
                </span>

            </div>
            """
        )


        # Audit Database

        st.html(
            """
            <div class="cp-status-row">

                <div class="cp-status-left">

                    <span class="cp-status-dot"></span>

                    <span>
                        Audit Database
                    </span>

                </div>

                <span class="cp-status-connected">
                    Connected
                </span>

            </div>
            """
        )


        # ====================================================
        # ABOUT
        # ====================================================

        st.html(
            """
            <div class="cp-sidebar-about">

                <div class="cp-sidebar-about-title">
                    🛡️ &nbsp; ControlPlane.ai
                </div>

                <div class="cp-sidebar-about-text">
                    The intelligent control layer between AI
                    generation and the end user.
                </div>

            </div>

            <div class="cp-sidebar-footer">
                © 2025 ControlPlane.ai
            </div>
            """
        )