from core.performance import PerformanceEngine
from core.responsible_ai import ResponsibleAIEngine
from core.context import ContextEngine
from core.cost import CostEngine
from core.risk import RiskEngine
from core.decision import DecisionEngine


# Create all engines

performance_engine = PerformanceEngine()

responsible_ai_engine = ResponsibleAIEngine()

context_engine = ContextEngine()

cost_engine = CostEngine()

risk_engine = RiskEngine()

decision_engine = DecisionEngine()


# User input

user_query = "Can a customer get a refund?"


# AI response

ai_response = """
Customers can receive a guaranteed full refund
at any time, even after five years.
"""


# 1. Performance Analysis

performance_result = performance_engine.analyze(
    user_query,
    ai_response
)


# 2. Responsible AI Analysis

responsible_result = responsible_ai_engine.analyze(
    ai_response
)


# 3. Context Analysis

context_result = context_engine.analyze(
    user_query,
    application_context="customer_service"
)


# 4. Cost Analysis

cost_result = cost_engine.analyze(
    user_query,
    ai_response
)


# 5. Risk Analysis

risk_result = risk_engine.analyze(
    performance_result["hallucination_risk"],
    responsible_result["risk_level"],
    context_result["context_risk"],
    cost_result["cost_risk"]
)


# 6. Final Decision

decision_result = decision_engine.decide(risk_result)


print("\nCONTROLPLANE.AI FINAL DECISION\n")

print("Hallucination Risk:", performance_result["hallucination_risk"])

print("Responsible AI Risk:", responsible_result["risk_level"])

print("Context Risk:", context_result["context_risk"])

print("Cost Risk:", cost_result["cost_risk"])

print("Total Risk Score:", risk_result["total_risk_score"])

print("Overall Risk:", decision_result["overall_risk"])

print("Decision:", decision_result["decision"])

print("Reason:", decision_result["reason"])