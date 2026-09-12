class CostEngine:

    def estimate_tokens(self, text):
        if not text:
            return 0

        return max(1, len(text) // 4)


    def analyze(self, user_query, ai_response):

        input_tokens = self.estimate_tokens(user_query)
        output_tokens = self.estimate_tokens(ai_response)

        total_tokens = input_tokens + output_tokens

        cost_per_1000_tokens = 0.01

        estimated_cost = (
            total_tokens / 1000
        ) * cost_per_1000_tokens


        if total_tokens > 5000:
            cost_risk = "HIGH"

        elif total_tokens > 2000:
            cost_risk = "MEDIUM"

        else:
            cost_risk = "LOW"


        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "estimated_cost": round(estimated_cost, 6),
            "cost_risk": cost_risk
        }