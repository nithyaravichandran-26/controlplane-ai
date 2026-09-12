class RiskEngine:

    # =================================
    # EXTRACT RISK VALUE
    # =================================

    def extract_risk(self, result, possible_keys):

        # If already a string
        if isinstance(result, str):

            return result.upper()


        # If result is a dictionary
        if isinstance(result, dict):

            for key in possible_keys:

                if key in result:

                    value = result[key]

                    if isinstance(value, str):

                        return value.upper()


            # Try common generic key
            for key in [
                "risk",
                "risk_level",
                "overall_risk"
            ]:

                if key in result:

                    value = result[key]

                    if isinstance(value, str):

                        return value.upper()


        # Safe fallback
        return "CRITICAL"


    # =================================
    # RISK SCORE
    # =================================

    def get_risk_score(self, risk):

        risk_scores = {

            "LOW": 1,

            "MEDIUM": 2,

            "HIGH": 3,

            "CRITICAL": 4

        }

        return risk_scores.get(
            risk.upper() if isinstance(risk, str) else "CRITICAL",
            4
        )


    # =================================
    # ANALYZE OVERALL RISK
    # =================================

    def analyze(
        self,
        hallucination_result,
        responsible_ai_result,
        context_result,
        cost_result,
        knowledge_result,
        policy_result
    ):

        # ---------------------------------
        # EXTRACT INDIVIDUAL RISKS
        # ---------------------------------

        hallucination_risk = self.extract_risk(
            hallucination_result,
            [
                "hallucination_risk",
                "risk"
            ]
        )


        responsible_ai_risk = self.extract_risk(
            responsible_ai_result,
            [
                "responsible_ai_risk",
                "risk"
            ]
        )


        context_risk = self.extract_risk(
            context_result,
            [
                "context_risk",
                "risk"
            ]
        )


        cost_risk = self.extract_risk(
            cost_result,
            [
                "cost_risk",
                "risk"
            ]
        )


        knowledge_risk = self.extract_risk(
            knowledge_result,
            [
                "knowledge_risk",
                "risk"
            ]
        )


        policy_risk = self.extract_risk(
            policy_result,
            [
                "policy_risk",
                "risk"
            ]
        )


        # ---------------------------------
        # INDIVIDUAL RISK SCORES
        # ---------------------------------

        hallucination_score = self.get_risk_score(
            hallucination_risk
        )


        responsible_ai_score = self.get_risk_score(
            responsible_ai_risk
        )


        context_score = self.get_risk_score(
            context_risk
        )


        cost_score = self.get_risk_score(
            cost_risk
        )


        knowledge_score = self.get_risk_score(
            knowledge_risk
        )


        policy_score = self.get_risk_score(
            policy_risk
        )


        # ---------------------------------
        # TOTAL RISK SCORE
        # ---------------------------------

        total_risk_score = (

            hallucination_score
            + responsible_ai_score
            + context_score
            + cost_score
            + knowledge_score
            + policy_score

        )


        # ---------------------------------
        # OVERALL RISK
        # ---------------------------------

        if total_risk_score <= 7:

            overall_risk = "LOW"


        elif total_risk_score <= 10:

            overall_risk = "MEDIUM"


        elif total_risk_score <= 15:

            overall_risk = "HIGH"


        else:

            overall_risk = "CRITICAL"


        # ---------------------------------
        # RETURN RESULT
        # ---------------------------------

        return {

            "hallucination_risk":
                hallucination_risk,

            "responsible_ai_risk":
                responsible_ai_risk,

            "context_risk":
                context_risk,

            "cost_risk":
                cost_risk,

            "knowledge_risk":
                knowledge_risk,

            "policy_risk":
                policy_risk,

            "hallucination_score":
                hallucination_score,

            "responsible_ai_score":
                responsible_ai_score,

            "context_score":
                context_score,

            "cost_score":
                cost_score,

            "knowledge_score":
                knowledge_score,

            "policy_score":
                policy_score,

            "total_risk_score":
                total_risk_score,

            "overall_risk":
                overall_risk

        }