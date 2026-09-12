class ContextEngine:

    def analyze(self, user_query, application_context="general"):

        application_context = application_context.lower()

        high_risk_contexts = [
            "hr",
            "healthcare",
            "medical",
            "finance",
            "legal"
        ]

        medium_risk_contexts = [
            "refund",
            "customer_support",
            "education"
        ]

        if application_context in high_risk_contexts:
            risk_level = "HIGH"

        elif application_context in medium_risk_contexts:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        return {
            "application_context": application_context,
            "context_risk": risk_level,
            "user_query": user_query
        }