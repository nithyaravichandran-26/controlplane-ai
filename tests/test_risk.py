from core.risk import RiskEngine


engine = RiskEngine()


result = engine.analyze(
    hallucination_risk="MEDIUM",
    responsible_ai_risk="HIGH",
    context_risk="HIGH",
    cost_risk="LOW"
)


print("\nRISK ENGINE ANALYSIS\n")

print(
    "Hallucination Risk:",
    result["hallucination_risk"]
)

print(
    "Responsible AI Risk:",
    result["responsible_ai_risk"]
)

print(
    "Context Risk:",
    result["context_risk"]
)

print(
    "Cost Risk:",
    result["cost_risk"]
)

print(
    "Total Risk Score:",
    result["total_risk_score"]
)

print(
    "Overall Risk:",
    result["overall_risk"]
)