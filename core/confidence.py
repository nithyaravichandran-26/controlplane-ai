class ConfidenceEngine:

    def analyze(
        self,
        hallucination_risk,
        responsible_ai_risk,
        context_risk,
        cost_risk,
        knowledge_risk,
        policy_risk
    ):

        # =================================
        # RISK SCORE MAPPING
        # =================================

        risk_scores = {

            "LOW": 0,

            "MEDIUM": 1,

            "HIGH": 2,

            "CRITICAL": 3

        }


        # =================================
        # INDIVIDUAL SCORES
        # =================================

        hallucination_score = risk_scores.get(
            hallucination_risk,
            2
        )

        responsible_ai_score = risk_scores.get(
            responsible_ai_risk,
            2
        )

        context_score = risk_scores.get(
            context_risk,
            2
        )

        cost_score = risk_scores.get(
            cost_risk,
            2
        )

        knowledge_score = risk_scores.get(
            knowledge_risk,
            2
        )

        policy_score = risk_scores.get(
            policy_risk,
            2
        )


        # =================================
        # TOTAL RISK
        # =================================

        total_risk = (

            hallucination_score
            + responsible_ai_score
            + context_score
            + cost_score
            + knowledge_score
            + policy_score

        )


        # =================================
        # MAXIMUM POSSIBLE RISK
        # =================================

        maximum_risk = 18


        # =================================
        # CONFIDENCE SCORE
        # =================================

        confidence_score = round(

            (
                (maximum_risk - total_risk)
                / maximum_risk
            ) * 100

        )


        # Keep score between 0 and 100

        confidence_score = max(
            0,
            min(
                100,
                confidence_score
            )
        )


        # =================================
        # CONFIDENCE LEVEL
        # =================================

        if confidence_score >= 80:

            confidence_level = "HIGH"

        elif confidence_score >= 50:

            confidence_level = "MEDIUM"

        else:

            confidence_level = "LOW"


        # =================================
        # RETURN
        # =================================

        return {

            "confidence_score":
                confidence_score,

            "confidence_level":
                confidence_level

        }