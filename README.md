# 🛡️ ControlPlane.ai

### AI Governance Control Layer for Safe, Context-Aware and Auditable AI

> **The intelligent control layer between AI generation and the end user.**

ControlPlane.ai is a prototype AI governance control layer that evaluates AI-generated responses before they reach an end user.

The platform evaluates each response across six governance dimensions:

- 🔍 Hallucination / Reliability
- 🛡️ Responsible AI
- 🏢 Application Context
- 💰 Cost
- 📚 Knowledge Grounding
- 📜 Policy Compliance

These evaluations are combined into a **risk score** and **confidence score**, followed by a governance decision:

**ALLOW · WARN · HUMAN REVIEW · BLOCK**

The platform also maintains an auditable record of governance decisions and provides a **human-in-the-loop workflow** for responses that require additional review.

---

## 🎯 Problem

As organizations increasingly adopt Generative AI across customer service, HR, finance, healthcare and other business workflows, generating an answer is only one part of the problem.

Organizations also need to determine:

- Is the response reliable?
- Is the response appropriate for the application context?
- Does it contain responsible-AI risks?
- Is it grounded in trusted organizational knowledge?
- Does it comply with applicable policies?
- How confident should the system be in the response?
- Should the response be released, warned, blocked, or reviewed by a human?
- Can the decision be audited later?

Without a governance layer, an AI response can move directly from generation to the end user without sufficient evaluation.

**ControlPlane.ai addresses this by introducing a governance control layer between AI generation and the end user.**

---

## 💡 Solution

### Traditional AI Workflow

```text
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  AI Model   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  End User   │
└─────────────┘
ControlPlane.ai Workflow
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  AI Model   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│          ControlPlane.ai            │
│         Governance Layer            │
├─────────────────────────────────────┤
│                                     │
│  • Hallucination / Reliability      │
│  • Responsible AI                   │
│  • Application Context              │
│  • Cost                             │
│  • Knowledge Grounding              │
│  • Policy Compliance                │
│                                     │
└──────────────────┬──────────────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Risk & Confidence    │
        │     Evaluation       │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Governance Decision  │
        └──────────┬───────────┘
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
    ALLOW        WARN     HUMAN REVIEW
                               │
                               ▼
                             BLOCK

The objective is to make AI responses evaluated, controlled and auditable before release.
```


## 🎥 Prototype Demonstration

Watch the ControlPlane.ai prototype in action, demonstrating the complete AI governance workflow — from AI response generation and six-dimensional risk analysis to confidence scoring, governance decisions, human review, and audit logging.

▶️ [Watch the Prototype Demo](https://drive.google.com/file/d/1Og6Q1E1-Jdf8jcKkeqUW0d2-fo9i2JPZ/view)



🔄 How It Works

Every AI response passes through a multi-stage governance workflow.

1. User Query

A user submits a query through the Live Simulator.

An application context can also be selected:

Customer Service
Finance
Healthcare
HR
General

2. AI Response Generation

The platform generates a response using the built-in local demo response generator.

An optional real-LLM path can also be enabled through configuration.

3. Six Governance Checks

The response is evaluated independently across:

Hallucination / Reliability
Responsible AI
Application Context
Cost
Knowledge Grounding
Policy Compliance

4. Risk Evaluation

The six risk results are aggregated into:

Total Risk Score
Overall Risk Level

5. Confidence Evaluation

The Confidence Engine converts the governance results into a score between 0 and 100.

6. Governance Decision

The Decision Engine applies policy-first and risk-based rules to produce one of four outcomes:

Decision	      Meaning
🟢 ALLOW	      Response passes governance checks
🟡 WARN	      Response can proceed with elevated risk
🟠 HUMAN REVIEW     Human approval is required
🔴 BLOCK	      Response should not be released

7. Audit Logging

Every evaluation is stored in a local SQLite database.

The audit record contains:

User Query
AI Response
Application Context
Hallucination Risk
Responsible AI Risk
Context Risk
Cost Risk
Knowledge Risk
Knowledge Status
Policy Risk
Policy Status
Confidence Score
Confidence Level
Total Risk Score
Overall Risk
Governance Decision
Reason
Timestamp

8. Human-in-the-Loop

Responses requiring human intervention appear in the Human Review queue.

A reviewer can inspect the complete analysis and make the final decision:

             HUMAN REVIEW
                  │
          ┌───────┴───────┐
          │               │
          ▼               ▼
      ✅ APPROVE       🚫 BLOCK
       RESPONSE        RESPONSE

✨ Key Capabilities

🧠 Multi-Dimensional Risk Analysis

ControlPlane.ai does not rely on a single risk signal.

Each response is evaluated across six independent governance dimensions:

Hallucination / Reliability
Responsible AI
Application Context
Cost
Knowledge Grounding
Policy Compliance

📚 Knowledge Grounding

The Knowledge Base Engine loads trusted organizational documents from:

data/knowledge_base/

The prototype uses TF-IDF and cosine similarity to identify the best-matching trusted document for a query.

This provides a grounding signal that can be used when evaluating reliability.

🛡️ Responsible AI Analysis

The Responsible AI Engine checks configured patterns for risks such as:

Personally identifiable information
Toxic language
Bias-indicator phrasing
Unsafe policy-related phrases

🏢 Application Context Awareness

The Context Engine evaluates risk based on the selected application context.

Supported contexts include:

Customer Service
Finance
Healthcare
HR
General

💰 Cost Risk

The Cost Engine estimates response usage and evaluates it against configured thresholds.

📜 Policy Compliance

The Policy Engine evaluates responses against configured policy rules.

The prototype supports:

Context-specific policy checks
Global critical-safety rules
Restricted-term detection

📊 Confidence Scoring

The Confidence Engine converts governance results into a 0–100 confidence score.

The confidence score represents a governance confidence measure and should not be interpreted as a statistically calibrated probability.

👤 Human-in-the-Loop Governance

High-risk responses can be routed to a human reviewer.

The reviewer can:

Inspect the complete analysis
Review the AI response
Examine individual risk dimensions
Review the confidence score
Review the automated decision
Approve the response
Block the response

🧾 Auditable Governance

Every evaluation is stored in SQLite.

The platform provides dedicated interfaces for:

Risk Dashboard
Audit Logs
Human Review

🏗️ Architecture

Component	         Responsibility

ResponseGenerator   -  Generates the response to be governed — local demo generator by default, with an optional real-LLM path

PerformanceEngine   -  Estimates hallucination/reliability risk using TF-IDF and cosine similarity against trusted knowledge

ResponsibleAIEngine -  Detects configured responsible-AI risk patterns including PII, toxic language, bias indicators and unsafe phrases

ContextEngine	      -  Evaluates risk based on the selected application context

CostEngine          -  Estimates response cost using configured token/cost thresholds

KnowledgeBase	      -  Loads trusted .txt documents and ranks them against the user query

PolicyEngine        -  Evaluates responses against context-specific and global policy rules

RiskEngine          -  Aggregates the six risk dimensions into a total risk score and overall risk level

ConfidenceEngine    -  Converts governance risk results into a 0–100 confidence score

DecisionEngine      -  Applies policy-first and risk-based rules to determine the final governance decision

database/db.py      -  Maintains the SQLite audit log and human-review state

📂 Project Structure
```text
controlplane_ai/
│
├── app.py
│
├── core/
│   ├── __init__.py
│   ├── confidence.py
│   ├── context.py
│   ├── cost.py
│   ├── decision.py
│   ├── knowledge.py
│   ├── performance.py
│   ├── policy.py
│   ├── response_generator.py
│   ├── responsible_ai.py
│   └── risk.py
│
├── data/
│   └── knowledge_base/
│       ├── company_policy.txt
│       ├── hr_policy.txt
│       ├── leave_policy.txt
│       ├── policies.txt
│       └── refund_policy.txt
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── pages/
│   ├── __init__.py
│   ├── audit_logs.py
│   ├── dashboard.py
│   ├── human_review.py
│   ├── shared_ui.py
│   └── simulator.py
│
├── policies/
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt
```

🖥️ Application Modules

🏠 Overview

Provides a high-level view of the ControlPlane.ai governance platform.

It displays:

Total analyses
Allowed responses
Blocked responses
Human review cases
Governance pipeline
System status
⚡ Live Simulator

The Live Simulator allows users to submit queries and observe the complete governance workflow.
```text
Query
 ↓
AI Response
 ↓
Risk Analysis
 ↓
Knowledge Check
 ↓
Policy Check
 ↓
Confidence
 ↓
Decision
 ↓
Audit Log
```

📊 Risk Dashboard

The Risk Dashboard provides an overview of historical governance evaluations.

It allows users to inspect risk scores, decisions and governance activity.

📋 Audit Logs

The Audit Logs interface provides access to stored governance evaluations.

Each analysis can be traced back to its:

Query
Response
Risk analysis
Confidence
Decision
Reason
Timestamp

👤 Human Review

The Human Review interface displays cases requiring manual governance approval.

Reviewers can inspect the complete evaluation and choose:

ALLOW
  or
BLOCK

⚙️ Requirements

The project requires:

Python 3.10 or later
Streamlit
pandas
scikit-learn

All required Python packages are listed in:

requirements.txt

No external API key is required to run the default prototype.

🚀 Installation

1. Clone the Repository
git clone https://github.com/DSruthiSarika/controlplane_ai.git

Move into the project directory:

cd controlplane_ai
2. Create a Virtual Environment
macOS / Linux
python3 -m venv .venv

Activate it:

source .venv/bin/activate
Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application
streamlit run app.py

Streamlit will provide a local URL, normally:

http://localhost:8501

Open the URL in your browser.

🔧 Configuration

The application works in demo mode without any external API key.

The default configuration uses the local demo response generator.

Optional Real LLM

If the optional real-LLM path is enabled, configure:

export USE_REAL_LLM=true
export OPENAI_API_KEY=<your-api-key>

With USE_REAL_LLM unset or set to false, the local demo generator is used.

Never commit API keys or other secrets to GitHub.

🧪 Testing

The repository contains a tests/ directory for testing the governance components.

The major end-to-end workflows can be validated through:

Live Simulator
Risk Dashboard
Audit Logs
Human Review

🛠️ Troubleshooting

Streamlit Cannot Find a Module

If you see an error such as:

ModuleNotFoundError: No module named 'core.context'

make sure you are running Streamlit from the project root:

cd controlplane_ai
streamlit run app.py

Also ensure the expected project structure is present.

Database Errors

If the application reports a database-related error, verify that:

database/
    __init__.py
    db.py

exists and that Streamlit is being launched from the project root.

Knowledge Grounding Returns High Risk

Verify that the following directory exists:

data/knowledge_base/

and contains the trusted .txt knowledge documents.

If the knowledge base is missing or empty, the system may not find a suitable grounding match.

Human Review Shows No Cases

Human Review only displays evaluations currently marked for human review.

Check the Risk Dashboard or Audit Logs to confirm the stored decision for the evaluation.

❓ FAQ
Do I need an OpenAI API key?

No.

The default prototype runs using the local demo response generator.

An API key is only required if the optional real-LLM path is enabled.

Why use rule-based governance checks?

Rule-based checks make governance decisions traceable to specific:

Terms
Thresholds
Similarity scores
Policy rules

This is useful for an auditable governance prototype and avoids adding another model call for every governance evaluation.

Is the hallucination detector a factuality checker?

No.

The prototype uses TF-IDF and cosine similarity against trusted knowledge.

High similarity can provide a grounding signal, but textual similarity does not prove factual correctness.

What happens to high-risk responses?

Depending on the risk and policy evaluation, a response may be:

ALLOW
WARN
HUMAN REVIEW
BLOCK

Responses routed to Human Review require a human decision before the final action is taken.

Where are the governance decisions stored?

The prototype uses SQLite.

The database stores the audit history of AI evaluations and governance decisions.

⚠️ Known Limitations

ControlPlane.ai is a prototype and is not intended to represent a production-grade enterprise governance system yet.

Hallucination Detection

Hallucination detection is currently similarity-based using TF-IDF.

High textual similarity does not guarantee factual correctness.

Responsible AI Detection

Responsible-AI detection uses predefined patterns and keywords.

It may not identify every indirect, contextual or emerging form of harmful content.

Policy Engine

Policy rules are currently hand-written and context-specific.

A production system would require a more sophisticated policy management and versioning framework.

Cost Estimation

Cost estimation is an approximation based on configured calculations rather than actual provider billing metadata.

Database

SQLite is appropriate for this prototype.

A production multi-user deployment would require a scalable managed database.

Confidence Score

The confidence score is a governance score derived from configured risk levels.

It is not a statistically calibrated probability.

🚀 Future Scope

Potential future development includes:

Enterprise-grade policy management
Policy versioning and approval workflows
Advanced semantic hallucination detection
More sophisticated responsible-AI evaluation
Real-time model monitoring
Multi-model governance
Role-based access control
Enterprise authentication
Scalable cloud database
Governance analytics and reporting
Model-specific risk profiles
Advanced explainability
Automated compliance reporting
Production-grade LLM integrations

These improvements can evolve the prototype toward a broader enterprise AI governance platform.

🌟 Why ControlPlane.ai?

ControlPlane.ai brings multiple governance signals together into a single control layer instead of treating AI safety, reliability, policy compliance, cost and auditability as separate concerns.

```text
AI Response
     ↓
Reliability + Responsible AI + Context
     ↓
Cost + Knowledge + Policy
     ↓
Risk Evaluation
     ↓
Confidence Score
     ↓
Governance Decision
     ↓
ALLOW / WARN / HUMAN REVIEW / BLOCK
     ↓
Audit Logging
```
This architecture demonstrates a practical approach to responsible, explainable and auditable AI governance.

👥 Team Sentinel

Digumurthy Sruthi Sarika

Nithya R

Khushi Kumari
