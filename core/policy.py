class PolicyEngine:

    def analyze(
        self,
        user_query,
        ai_response,
        application_context
    ):

        # ---------------------------------
        # CONVERT INPUT TO LOWERCASE
        # ---------------------------------

        query = user_query.lower()

        response = ai_response.lower()


        # ---------------------------------
        # DEFAULT POLICY RESULT
        # ---------------------------------

        policy_risk = "LOW"

        policy_status = "COMPLIANT"

        violations = []


        # ---------------------------------
        # HEALTHCARE POLICY
        # ---------------------------------

        if application_context == "healthcare":

            restricted_terms = [
                "diagnose",
                "diagnosis",
                "prescribe",
                "prescription",
                "dosage",
                "take this medicine"
            ]


            for term in restricted_terms:

                if term in query or term in response:

                    policy_risk = "HIGH"

                    policy_status = "REVIEW REQUIRED"

                    violations.append(
                        f"Medical advice policy triggered: {term}"
                    )


        # ---------------------------------
        # FINANCE POLICY
        # ---------------------------------

        elif application_context == "finance":

            restricted_terms = [
                "buy this stock",
                "sell this stock",
                "guaranteed profit",
                "guaranteed return",
                "invest all your money",
                "financial advice"
            ]


            for term in restricted_terms:

                if term in query or term in response:

                    policy_risk = "HIGH"

                    policy_status = "REVIEW REQUIRED"

                    violations.append(
                        f"Financial advice policy triggered: {term}"
                    )


        # ---------------------------------
        # HR POLICY
        # ---------------------------------

        elif application_context == "hr":

            restricted_terms = [
                "employee salary",
                "salary details",
                "personal information",
                "private employee data",
                "confidential employee",
                "employee records"
            ]


            for term in restricted_terms:

                if term in query or term in response:

                    policy_risk = "HIGH"

                    policy_status = "RESTRICTED"

                    violations.append(
                        f"Sensitive HR data policy triggered: {term}"
                    )


        # ---------------------------------
        # CUSTOMER SERVICE POLICY
        # ---------------------------------

        elif application_context == "customer_service":

            restricted_terms = [
                "password",
                "otp",
                "credit card number",
                "cvv",
                "bank account number",
                "security code"
            ]


            for term in restricted_terms:

                if term in query or term in response:

                    policy_risk = "HIGH"

                    policy_status = "RESTRICTED"

                    violations.append(
                        f"Sensitive customer data policy triggered: {term}"
                    )


        # ---------------------------------
        # GENERAL CRITICAL SAFETY POLICY
        # ---------------------------------

        critical_terms = [
            "make a bomb",
            "build a bomb",
            "kill someone",
            "harm someone",
            "attack someone",
            "suicide instructions"
        ]


        for term in critical_terms:

            if term in query or term in response:

                policy_risk = "CRITICAL"

                policy_status = "VIOLATION"

                violations.append(
                    f"Critical safety policy violation: {term}"
                )


        # ---------------------------------
        # RETURN POLICY RESULT
        # ---------------------------------

        return {

            "policy_risk": policy_risk,

            "policy_status": policy_status,

            "violations": violations,

            "violation_count": len(
                violations
            )
        }