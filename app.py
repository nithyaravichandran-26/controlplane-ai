import streamlit as st

from pages.shared_ui import apply_theme, sidebar

# ============================================================
# DATABASE
# ============================================================

try:
    from database.db import get_all_logs
except Exception:
    get_all_logs = None


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ControlPlane.ai",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SHARED CONTROLPLANE.AI UI
# ============================================================

apply_theme()
sidebar("overview")


# ============================================================
# OVERVIEW PAGE CSS
# IMPORTANT:
# Sidebar CSS is NOT here.
# Sidebar is handled by shared_ui.py
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN PAGE
       ======================================================== */

    .block-container {
        max-width: 1500px !important;
        padding-top: 34px !important;
        padding-right: 18px !important;
        padding-bottom: 55px !important;
        padding-left: 18px !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 14px !important;
        align-items: stretch !important;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .cp-hero {
        position: relative;
        width: 100%;
        height: 300px;
        overflow: hidden;
        box-sizing: border-box;

        border-radius: 20px;

        border: 1px solid rgba(31, 145, 244, 0.65);

        background:
            radial-gradient(
                circle at 79% 48%,
                rgba(0, 124, 255, 0.20),
                transparent 24%
            ),
            linear-gradient(
                110deg,
                #061d35 0%,
                #041526 55%,
                #020b15 100%
            );

        box-shadow:
            0 0 35px rgba(0, 104, 255, 0.09),
            inset 0 0 50px rgba(0, 72, 145, 0.06);
    }


    /* ========================================================
       HERO CONTENT
       ======================================================== */

    .cp-hero-content {
        position: relative;
        z-index: 10;

        width: 57%;
        box-sizing: border-box;

        padding: 30px 30px 28px;
    }


    .cp-hero-kicker {
        display: inline-flex;
        align-items: center;

        white-space: nowrap;

        color: #62c0ff;

        background: rgba(12, 116, 202, 0.16);

        border: 1px solid rgba(44, 163, 255, 0.55);

        border-radius: 999px;

        padding: 8px 15px;

        font-size: 0.61rem;
        line-height: 1;

        font-weight: 900;

        letter-spacing: 0.105em;
    }


    .cp-hero-title {
        margin-top: 17px;

        color: #f8fbff;

        font-size: 3.25rem;

        line-height: 1;

        letter-spacing: -0.055em;

        font-weight: 950;
    }


    .cp-hero-title .accent {
        color: #31aaff;
    }


    .cp-hero-lead {
        color: #32aaff;

        font-size: 0.92rem;

        line-height: 1.35;

        font-weight: 800;

        margin-top: 14px;
    }


    .cp-hero-description {
        color: #c0cddd;

        font-size: 0.84rem;

        line-height: 1.52;

        max-width: 690px;

        margin-top: 15px;
    }


    .cp-online-pill {
        display: inline-flex;
        align-items: center;

        gap: 8px;

        margin-top: 17px;

        padding: 8px 15px;

        border-radius: 999px;

        color: #1bed82;

        background: rgba(9, 220, 119, 0.07);

        border: 1px solid rgba(13, 225, 126, 0.30);

        font-size: 0.63rem;

        font-weight: 900;
    }


    .cp-online-dot {
        width: 10px;
        height: 10px;

        border-radius: 50%;

        background: #14dd6a;

        box-shadow:
            0 0 9px rgba(20, 221, 106, 0.80);
    }


    /* ========================================================
       HERO VISUAL
       ======================================================== */

    .cp-hero-visual {
        position: absolute;

        z-index: 2;

        right: 0;
        top: 0;

        width: 48%;
        height: 100%;
    }


    .cp-hero-glow {
        position: absolute;

        right: 24%;
        top: 38%;

        width: 220px;
        height: 120px;

        border-radius: 50%;

        background: rgba(0, 145, 255, 0.20);

        filter: blur(38px);
    }


    .cp-orbit {
        position: absolute;

        right: 0%;
        top: 52%;

        width: 610px;
        height: 150px;

        transform:
            translateY(-50%)
            rotate(-3deg);

        border: 1px solid rgba(28, 148, 255, 0.48);

        border-radius: 50%;

        box-shadow:
            0 0 25px rgba(0, 136, 255, 0.10);
    }


    .cp-orbit.two {
        right: 7%;
        width: 505px;
        height: 100px;

        opacity: 0.75;
    }


    .cp-orbit.three {
        right: 16%;
        width: 350px;
        height: 58px;

        opacity: 0.55;
    }


    .cp-orbit::before,
    .cp-orbit::after {
        content: "";

        position: absolute;

        border-radius: 50%;

        background: #1fa7ff;

        box-shadow:
            0 0 11px #1fa7ff,
            0 0 25px rgba(31, 167, 255, 0.65);
    }


    .cp-orbit::before {
        width: 6px;
        height: 6px;

        left: 15%;
        top: 47%;
    }


    .cp-orbit::after {
        width: 4px;
        height: 4px;

        right: 17%;
        top: 30%;
    }


    /* ========================================================
   HERO SHIELD
   ======================================================== */

    .cp-shield {
        position: absolute;

        left: 50%;
        top: 50%;

        transform: translate(-50%, -50%);

        width: 132px;
        height: 160px;

        display: flex;
        align-items: center;
        justify-content: center;

        box-sizing: border-box;

        /* OUTER SHIELD */
        background:
            linear-gradient(
                145deg,
                #1684ce 0%,
                #0861a5 58%,
                #06365f 100%
            );

        border: 2px solid #1caaff;

        clip-path: polygon(
            50% 0%,
            91% 15%,
            86% 57%,
            79% 73%,
            68% 88%,
            50% 100%,
            32% 88%,
            21% 73%,
            14% 57%,
            9% 15%
        );

        filter:
            drop-shadow(
                0 0 10px rgba(20, 166, 255, 0.85)
            )
            drop-shadow(
                0 0 25px rgba(0, 126, 255, 0.45)
            )
            drop-shadow(
                0 0 45px rgba(0, 126, 255, 0.20)
            );
    }


    /* ========================================================
    INNER SHIELD
    ======================================================== */

    .cp-shield-inner {
        position: absolute;

        left: 10px;
        right: 10px;
        top: 10px;
        bottom: 10px;

        display: flex;
        align-items: center;
        justify-content: center;

        box-sizing: border-box;

        /* IMPORTANT:
            Give the inner shield its own visible surface */
        background:
            linear-gradient(
                145deg,
                #0b65aa 0%,
                #08487d 55%,
                #031c34 100%
            );
  
        border: 2px solid rgba(28, 170, 255, 0.75);

        clip-path: polygon(
            50% 0%,
            91% 15%,
            86% 56%,
            77% 75%,
            50% 100%,
            23% 75%,
            14% 56%,
            9% 15%
        );

        box-shadow:
            inset 0 0 12px rgba(0, 80, 140, 0.35);
    }


    /* ========================================================
    CHECK MARK
    ======================================================== */

    .cp-shield-check {
        position: relative;
        z-index: 5;

        color: #45c5ff;

        font-size: 62px;

        font-weight: 900;

        line-height: 1;

        transform: translateY(-2px);

        text-shadow:
            0 0 5px #42c4ff,
            0 0 12px #24b8ff,
            0 0 25px rgba(36, 184, 255, 0.95);
    }

    /* ========================================================
       SECTION HEADINGS
       ======================================================== */

    .cp-section-head {
        margin: 28px 0 15px;
        padding-left: 2px;
    }


    .cp-section-title {
        color: #f2f7fc;

        font-size: 1.48rem;

        line-height: 1.2;

        font-weight: 900;

        letter-spacing: -0.025em;
    }


    .cp-section-subtitle {
        color: #7e91a6;

        font-size: 0.70rem;

        line-height: 1.4;

        margin-top: 7px;
    }


    /* ========================================================
       METRIC CARDS
       ======================================================== */

    .cp-metric-card {
        min-height: 155px;

        box-sizing: border-box;

        padding: 16px;

        border-radius: 15px;

        border: 1px solid rgba(44, 139, 218, 0.34);

        background:
            linear-gradient(
                145deg,
                rgba(6, 27, 46, 0.98),
                rgba(2, 12, 22, 0.98)
            );
    }


    .cp-metric-icon {
        width: 46px;
        height: 46px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 11px;

        background: #082d50;

        font-size: 22px;

        margin-bottom: 10px;
    }


    .cp-metric-label {
        color: #b9c7d7;

        font-size: 0.72rem;

        line-height: 1.2;
    }


    .cp-metric-value {
        color: #f5f8fc;

        font-size: 1.78rem;

        line-height: 1;

        font-weight: 950;

        margin-top: 7px;
    }


    .cp-metric-note {
        font-size: 0.68rem;

        line-height: 1.2;

        margin-top: 11px;
    }


    .cp-blue {
        color: #25aeff;
    }

    .cp-green {
        color: #18e980;
    }

    .cp-red {
        color: #ff5360;
    }

    .cp-orange {
        color: #ffac21;
    }


    /* ========================================================
       GOVERNANCE PIPELINE
       ======================================================== */

    .cp-pipeline-wrap {
        width: 100%;

        box-sizing: border-box;

        margin-top: 24px;
        margin-bottom: 10px;

        padding: 18px 18px 19px;

        border-radius: 16px;

        border: 1px solid rgba(39, 132, 210, 0.34);

        background:
            linear-gradient(
                145deg,
                rgba(5, 23, 40, 0.98),
                rgba(2, 11, 20, 0.98)
            );
    }


    .cp-pipeline-heading {
        color: #eef4fb;

        font-size: 1.02rem;

        line-height: 1.2;

        font-weight: 900;
    }


    .cp-pipeline-subheading {
        color: #72859a;

        font-size: 0.66rem;

        line-height: 1.35;

        margin-top: 5px;

        margin-bottom: 19px;
    }


    .cp-pipeline-grid {
        display: grid;

        grid-template-columns:
            minmax(120px, 1fr)
            36px
            minmax(120px, 1fr)
            36px
            minmax(120px, 1fr)
            36px
            minmax(120px, 1fr)
            36px
            minmax(120px, 1fr)
            36px
            minmax(120px, 1fr);

        align-items: start;

        width: 100%;
    }


    .cp-pipeline-node {
        min-width: 0;

        text-align: center;

        padding: 2px 4px 5px;
    }


    .cp-pipeline-icon {
        width: 58px;
        height: 58px;

        margin: 0 auto 10px;

        display: flex;

        align-items: center;
        justify-content: center;

        border-radius: 13px;

        background:
            linear-gradient(
                145deg,
                #0d3a63,
                #061b31
            );

        border: 1px solid rgba(33, 157, 250, 0.52);

        box-shadow:
            inset 0 0 18px rgba(0, 121, 220, 0.10);

        font-size: 25px;
    }


    .cp-pipeline-name {
        color: #edf3fa;

        font-size: 0.68rem;

        line-height: 1.2;

        font-weight: 850;

        white-space: nowrap;
    }


    .cp-pipeline-desc {
        color: #718398;

        font-size: 0.58rem;

        line-height: 1.4;

        margin-top: 7px;

        min-height: 35px;
    }


    .cp-pipeline-arrow {
        height: 70px;

        display: flex;

        align-items: center;
        justify-content: center;

        color: #a4b4c7;

        font-size: 1.25rem;
    }


    /* ========================================================
       CAPABILITIES
       ======================================================== */

    .cp-capabilities-grid {
        display: grid;

        grid-template-columns:
            repeat(6, minmax(0, 1fr));

        gap: 10px;

        margin-top: 12px;
    }


    .cp-cap-card {
        min-height: 145px;

        box-sizing: border-box;

        padding: 13px;

        border-radius: 13px;

        border: 1px solid rgba(40, 132, 210, 0.27);

        background:
            linear-gradient(
                145deg,
                rgba(5, 24, 41, 0.97),
                rgba(2, 12, 21, 0.98)
            );
    }


    .cp-cap-icon {
        font-size: 22px;

        line-height: 1;

        margin-bottom: 10px;
    }


    .cp-cap-title {
        color: #eef4fa;

        font-size: 0.68rem;

        font-weight: 850;

        line-height: 1.2;
    }


    .cp-cap-text {
        color: #73859a;

        font-size: 0.57rem;

        line-height: 1.5;

        margin-top: 7px;
    }


    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 1200px) {

        .cp-hero-content {
            width: 62%;
        }

        .cp-hero-visual {
            width: 45%;
        }

        .cp-orbit {
            right: -18%;
        }

        .cp-orbit.two {
            right: -10%;
        }

        .cp-orbit.three {
            right: 0;
        }

        .cp-capabilities-grid {
            grid-template-columns:
                repeat(3, minmax(0, 1fr));
        }
    }


    @media (max-width: 900px) {

        .block-container {
            padding:
                24px 14px 45px !important;
        }

        .cp-hero {
            height: 355px;
        }

        .cp-hero-content {
            width: 100%;
        }

        .cp-hero-visual {
            width: 100%;
            opacity: 0.24;
        }

        .cp-hero-title {
            font-size: 2.7rem;
        }

        .cp-pipeline-grid {
            grid-template-columns:
                repeat(2, minmax(0, 1fr));

            gap: 18px;
        }

        .cp-pipeline-arrow {
            display: none;
        }
    }


    @media (max-width: 650px) {

        .cp-capabilities-grid {
            grid-template-columns: 1fr;
        }

        .cp-pipeline-grid {
            grid-template-columns: 1fr;
        }

        .cp-metric-card {
            min-height: 145px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# GET DATABASE DATA
# ============================================================

logs = []

if get_all_logs:

    try:
        logs = get_all_logs() or []

    except Exception:
        logs = []


# ============================================================
# CALCULATE COUNTS
# ============================================================

total = len(logs)

allowed = 0
blocked = 0
human_review = 0


for row in logs:

    try:

        if len(row) > 16:

            decision = str(row[16]).upper().strip()

            if decision in (
                "ALLOW",
                "ALLOWED",
            ):

                allowed += 1

            elif decision in (
                "BLOCK",
                "BLOCKED",
            ):

                blocked += 1

            elif "HUMAN REVIEW" in decision or "REVIEW" in decision:

                human_review += 1

    except Exception:
        continue


def pct(value):

    if total == 0:
        return 0

    return (value / total) * 100


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="cp-hero">

        <div class="cp-hero-content">

            <div class="cp-hero-kicker">
                🛡 &nbsp; ENTERPRISE AI GOVERNANCE PLATFORM
            </div>

            <div class="cp-hero-title">
                ControlPlane<span class="accent">.ai</span>
            </div>

            <div class="cp-hero-lead">
                The intelligent control layer between AI generation
                and the end user.
            </div>

            <div class="cp-hero-description">
                ControlPlane.ai evaluates AI responses for reliability,
                safety, context, cost, knowledge grounding and policy
                compliance before they are released.
            </div>

            <div class="cp-online-pill">
                <span class="cp-online-dot"></span>
                GOVERNANCE ENGINE ONLINE
            </div>

        </div>


        <div class="cp-hero-visual">

            <div class="cp-hero-glow"></div>

            <div class="cp-orbit"></div>

            <div class="cp-orbit two"></div>

            <div class="cp-orbit three"></div>

            <div class="cp-shield">

                <div class="cp-shield-inner">

                    <div class="cp-shield-check">
                        ✓
                    </div>

                </div>

            </div>

        </div>

    </div>
    """
)


# ============================================================
# PLATFORM AT A GLANCE
# ============================================================

st.html(
    """
    <div class="cp-section-head">

        <div class="cp-section-title">
            📊 Platform at a Glance
        </div>

        <div class="cp-section-subtitle">
            Real-time overview of AI governance activity
        </div>

    </div>
    """
)


# ============================================================
# METRIC CARDS
# ============================================================

m1, m2, m3, m4 = st.columns(
    4,
    gap="small",
)


metric_data = [
    (
        m1,
        "📈",
        "Total Analyses",
        total,
        "Governance evaluations",
        "cp-blue",
    ),
    (
        m2,
        "🟢",
        "Allowed",
        allowed,
        f"{pct(allowed):.1f}% of analyses",
        "cp-green",
    ),
    (
        m3,
        "🛑",
        "Blocked",
        blocked,
        f"{pct(blocked):.1f}% of analyses",
        "cp-red",
    ),
    (
        m4,
        "👤",
        "Human Review",
        human_review,
        f"{pct(human_review):.1f}% of analyses",
        "cp-orange",
    ),
]


for (
    col,
    icon,
    label,
    value,
    note,
    cls,
) in metric_data:

    with col:

        st.html(
            f"""
            <div class="cp-metric-card">

                <div class="cp-metric-icon">
                    {icon}
                </div>

                <div class="cp-metric-label">
                    {label}
                </div>

                <div class="cp-metric-value">
                    {value}
                </div>

                <div class="cp-metric-note {cls}">
                    {note}
                </div>

            </div>
            """
        )


# ============================================================
# GOVERNANCE PIPELINE
# ============================================================

pipeline = [
    (
        "👤",
        "1. User Query",
        "User submits<br>a request",
    ),
    (
        "🤖",
        "2. AI Response",
        "AI model generates<br>a response",
    ),
    (
        "🔎",
        "3. Risk Engines",
        "6 specialized engines<br>analyze the response",
    ),
    (
        "🎯",
        "4. Risk Score",
        "Overall risk score<br>is calculated",
    ),
    (
        "🛡️",
        "5. Decision",
        "Allow, Review<br>or Block",
    ),
    (
        "📋",
        "6. Audit Log",
        "Decision & data<br>are recorded",
    ),
]


pipeline_html = """
<div class="cp-pipeline-wrap">

    <div class="cp-pipeline-heading">
        Governance Pipeline
    </div>

    <div class="cp-pipeline-subheading">
        Every AI response passes through our comprehensive
        governance workflow.
    </div>

    <div class="cp-pipeline-grid">
"""


for index, (
    icon,
    title,
    description,
) in enumerate(pipeline):

    pipeline_html += f"""
        <div class="cp-pipeline-node">

            <div class="cp-pipeline-icon">
                {icon}
            </div>

            <div class="cp-pipeline-name">
                {title}
            </div>

            <div class="cp-pipeline-desc">
                {description}
            </div>

        </div>
    """

    if index < len(pipeline) - 1:

        pipeline_html += """
        <div class="cp-pipeline-arrow">
            →
        </div>
        """


pipeline_html += """
    </div>

</div>
"""


st.html(pipeline_html)


# ============================================================
# PLATFORM CAPABILITIES
# ============================================================

st.html(
    """
    <div class="cp-section-head">

        <div class="cp-section-title">
            ⚙️ Platform Capabilities
        </div>

        <div class="cp-section-subtitle">
            A model-agnostic governance layer for responsible AI
        </div>

    </div>
    """
)


capabilities = [
    (
        "🧠",
        "Risk Analysis",
        "Evaluate hallucination, responsible AI, context, cost, knowledge and policy risks.",
    ),
    (
        "📚",
        "Knowledge Grounding",
        "Determine whether the response is supported by the knowledge base.",
    ),
    (
        "📜",
        "Policy Compliance",
        "Check responses against organizational policies and governance requirements.",
    ),
    (
        "🎯",
        "AI Confidence",
        "Convert multiple governance signals into an interpretable confidence score.",
    ),
    (
        "👤",
        "Human-in-the-Loop",
        "Escalate high-risk responses to human reviewers for safe decision making.",
    ),
    (
        "📋",
        "Auditability",
        "Record all evaluations, scores, decisions and governance outcomes.",
    ),
]


capabilities_html = """
<div class="cp-capabilities-grid">
"""


for (
    icon,
    title,
    text,
) in capabilities:

    capabilities_html += f"""
        <div class="cp-cap-card">

            <div class="cp-cap-icon">
                {icon}
            </div>

            <div class="cp-cap-title">
                {title}
            </div>

            <div class="cp-cap-text">
                {text}
            </div>

        </div>
    """


capabilities_html += """
</div>
"""


st.html(capabilities_html)
