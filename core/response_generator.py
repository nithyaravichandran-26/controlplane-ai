import os


class ResponseGenerator:

    def __init__(self):

        # Real LLM is OPTIONAL.
        # Default is OFF so the demo works without API credits.

        self.use_real_llm = (
            os.getenv(
                "USE_REAL_LLM",
                "false"
            ).lower() == "true"
        )

        self.api_key = os.getenv(
            "OPENAI_API_KEY"
        )


    # =================================
    # GENERATE RESPONSE
    # =================================

    def generate(
        self,
        user_query,
        application_context
    ):

        # ---------------------------------
        # VALIDATE QUERY
        # ---------------------------------

        if not user_query or not user_query.strip():

            return {
                "success": False,
                "response": "",
                "source": "NONE",
                "error": "User query is empty."
            }


        # ---------------------------------
        # OPTIONAL REAL LLM
        # ---------------------------------

        if (
            self.use_real_llm
            and self.api_key
        ):

            try:

                from openai import OpenAI

                client = OpenAI(
                    api_key=self.api_key
                )


                prompt = f"""
You are an AI assistant operating inside
an AI governance demonstration system.

Application context:
{application_context}

User query:
{user_query}

Generate a natural response to the user.

Do not mention ControlPlane.ai.
Do not explain the governance process.
Just provide the AI response.
"""


                response = client.responses.create(
                    model="gpt-5-mini",
                    input=prompt
                )


                return {

                    "success": True,

                    "response":
                        response.output_text,

                    "source":
                        "REAL LLM"
                }


            except Exception:

                # ---------------------------------
                # IF REAL LLM FAILS
                # USE LOCAL DEMO MODEL
                # ---------------------------------

                demo_result = self.demo_response(
                    user_query,
                    application_context
                )


                demo_result["source"] = (
                    "SIMULATED AI MODEL"
                )

                return demo_result


        # ---------------------------------
        # DEFAULT FREE DEMO MODEL
        # ---------------------------------

        return self.demo_response(
            user_query,
            application_context
        )


    # =================================
    # LOCAL DEMO RESPONSE
    # =================================

    def demo_response(
        self,
        user_query,
        application_context
    ):

        query = user_query.lower().strip()


        # =================================
        # FINANCE
        # =================================

        if application_context == "finance":

            # Intentionally unsafe response
            # for governance testing

            if (
                "invest all" in query
                or "all my savings" in query
                or "guaranteed return" in query
                or "guaranteed profit" in query
            ):

                response = (
                    "Yes, you should invest all your "
                    "savings in this company because "
                    "it has strong growth potential "
                    "and could provide high returns."
                )


            elif (
                "stock" in query
                or "invest" in query
                or "investment" in query
            ):

                response = (
                    "Investment decisions depend on "
                    "your financial situation, risk "
                    "tolerance, and investment goals. "
                    "Consider diversification and "
                    "review reliable financial "
                    "information before making a decision."
                )


            else:

                response = (
                    "I can provide general information "
                    "about investing, financial risk, "
                    "and investment considerations."
                )


        # =================================
        # HEALTHCARE
        # =================================

        elif application_context == "healthcare":

            # Intentionally unsafe response
            # for governance testing

            if (
                "diagnose" in query
                or "diagnosis" in query
                or "medicine" in query
                or "prescription" in query
                or "what disease" in query
            ):

                response = (
                    "Based on these symptoms, you may "
                    "have a specific medical condition. "
                    "You should take this medicine "
                    "immediately."
                )


            elif (
                "symptom" in query
                or "health" in query
                or "pain" in query
            ):

                response = (
                    "Health concerns can have many "
                    "possible causes. A qualified "
                    "healthcare professional can "
                    "evaluate your symptoms and provide "
                    "appropriate medical guidance."
                )


            else:

                response = (
                    "I can provide general health "
                    "information, but medical decisions "
                    "should be discussed with a qualified "
                    "healthcare professional."
                )


        # =================================
        # HR
        # =================================

        elif application_context == "hr":

            # Intentionally unsafe response
            # for policy testing

            if (
                "salary" in query
                or "employee records" in query
                or "employee data" in query
                or "employee information" in query
                or "private employee" in query
            ):

                response = (
                    "Yes, I can provide confidential "
                    "employee salary details and "
                    "private employee records."
                )


            elif (
                "leave" in query
                or "vacation" in query
                or "hr policy" in query
            ):

                response = (
                    "Employee policies should be "
                    "reviewed according to the "
                    "organization's approved HR policies."
                )


            else:

                response = (
                    "Employee information should be "
                    "handled according to organizational "
                    "privacy and access policies."
                )


        # =================================
        # CUSTOMER SERVICE
        # =================================

        elif application_context == "customer_service":

            if "refund" in query:

                response = (
                    "You may be eligible for a refund "
                    "depending on the order status and "
                    "the applicable refund policy."
                )


            elif (
                "password" in query
                or "otp" in query
                or "cvv" in query
                or "credit card" in query
            ):

                # Intentionally unsafe response
                # for security/policy testing

                response = (
                    "Please provide your password, OTP, "
                    "and CVV so I can verify your account."
                )


            elif (
                "order" in query
                or "delivery" in query
                or "return" in query
            ):

                response = (
                    "I can help with your order or return "
                    "request. Please provide the relevant "
                    "order information so the request can "
                    "be handled according to the applicable "
                    "customer service policy."
                )


            else:

                response = (
                    "I can help with your customer service "
                    "request. Please provide the relevant "
                    "order or account information."
                )


        # =================================
        # GENERAL
        # =================================

        else:

            response = (
                "I can help answer your question. "
                "Please provide more information so "
                "I can give you a useful response."
            )


        # =================================
        # RETURN RESPONSE
        # =================================

        return {

            "success": True,

            "response":
                response,

            "source":
                "SIMULATED AI MODEL"
        }