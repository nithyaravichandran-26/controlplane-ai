class DecisionEngine:

    def decide(
        self,
        risk_result,
        policy_result
    ):

        # ---------------------------------
        # GET RISK AND POLICY RESULTS
        # ---------------------------------

        overall_risk = risk_result["overall_risk"]

        policy_risk = policy_result["policy_risk"]

        policy_status = policy_result["policy_status"]

        violations = policy_result["violations"]


        # ---------------------------------
        # CRITICAL POLICY VIOLATION
        # ---------------------------------

        if policy_risk == "CRITICAL":

            decision = "BLOCK"

            reason = (
                "Critical policy violation detected. "
                "The AI response is blocked."
            )


        # ---------------------------------
        # HIGH POLICY RISK
        # ---------------------------------

        elif policy_risk == "HIGH":

            if policy_status == "RESTRICTED":

                decision = "BLOCK"

                reason = (
                    "Restricted policy violation detected. "
                    "The AI response contains sensitive "
                    "or restricted information."
                )


            else:

                decision = "HUMAN REVIEW"

                reason = (
                    "High-risk policy issue detected. "
                    "Human review is required before "
                    "the response can be allowed."
                )


        # ---------------------------------
        # NORMAL RISK-BASED DECISION
        # ---------------------------------

        elif overall_risk == "LOW":

            decision = "ALLOW"

            reason = (
                "Low overall risk detected. "
                "The AI response can be allowed."
            )


        elif overall_risk == "MEDIUM":

            decision = "WARN"

            reason = (
                "Medium overall risk detected. "
                "The response requires caution."
            )


        elif overall_risk == "HIGH":

            decision = "HUMAN REVIEW"

            reason = (
                "High overall risk detected. "
                "Human review is required."
            )


        else:

            decision = "BLOCK"

            reason = (
                "Critical or unknown risk detected. "
                "The AI response is blocked."
            )


        # ---------------------------------
        # RETURN FINAL RESULT
        # ---------------------------------

        return {

            "decision": decision,

            "reason": reason,

            "overall_risk": overall_risk,

            "policy_risk": policy_risk,

            "policy_status": policy_status,

            "violations": violations

        }