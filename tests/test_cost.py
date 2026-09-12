from core.cost import CostEngine


engine = CostEngine()


user_query = """
Can a customer get a refund after purchasing a product?
"""


ai_response = """
Customers can request a refund depending on the company's
refund policy and eligibility requirements.
"""


result = engine.analyze(
    user_query,
    ai_response
)


print("\nCOST ANALYSIS\n")

print("Input Tokens:",
      result["input_tokens"])

print("Output Tokens:",
      result["output_tokens"])

print("Total Tokens:",
      result["total_tokens"])

print("Estimated Cost: $",
      result["estimated_cost"])

print("Cost Risk:",
      result["cost_risk"])