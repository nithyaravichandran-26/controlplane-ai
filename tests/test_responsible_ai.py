from core.responsible_ai import ResponsibleAIEngine


engine = ResponsibleAIEngine()


ai_response = """
You are stupid.

Please contact john@gmail.com
or call 9876543210.

You are guaranteed a refund.
"""


result = engine.analyze(ai_response)


print("\nRESPONSIBLE AI ANALYSIS\n")

print("PII Detected:", result["pii_detected"])
print("PII Findings:", result["pii_findings"])

print("\nToxicity Detected:", result["toxicity_detected"])
print("Toxicity Findings:", result["toxicity_findings"])

print("\nBias Detected:", result["bias_detected"])
print("Bias Findings:", result["bias_findings"])

print("\nPolicy Violation Detected:",
      result["policy_violation_detected"])

print("Policy Findings:",
      result["policy_findings"])

print("\nTotal Issues:", result["total_issues"])

print("Responsible AI Risk:",
      result["risk_level"])