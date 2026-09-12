from core.context import ContextEngine


engine = ContextEngine()


user_query = "Should this employee be approved for promotion?"

result = engine.analyze(
    user_query,
    application_context="hr"
)


print("\nCONTEXT ANALYSIS\n")

print("Application Context:",
      result["application_context"])

print("Context Risk:",
      result["context_risk"])

print("User Query:",
      result["user_query"])