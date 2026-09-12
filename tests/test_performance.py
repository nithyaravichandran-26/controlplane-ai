from core.performance import PerformanceEngine


engine = PerformanceEngine()


user_query = "Can a customer get a refund?"


ai_response = """
Customers can receive a guaranteed full refund
at any time, even after five years.
"""


result = engine.analyze(
    user_query,
    ai_response
)


print("\nPERFORMANCE ANALYSIS\n")

print("Evidence Score:", result["evidence_score"])

print("Hallucination Risk:", result["hallucination_risk"])

print("Trusted Document:", result["trusted_document"])

print("Reason:", result["reason"])