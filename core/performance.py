from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from core.knowledge import KnowledgeBase


class PerformanceEngine:

    def __init__(self):

        self.knowledge_base = KnowledgeBase()


    # ---------------------------------
    # ANALYZE AI RESPONSE
    # ---------------------------------

    def analyze(
        self,
        user_query,
        ai_response
    ):

        # ---------------------------------
        # SEARCH TRUSTED KNOWLEDGE
        # ---------------------------------

        search_results = self.knowledge_base.search(
            user_query,
            top_k=1
        )


        # ---------------------------------
        # NO TRUSTED KNOWLEDGE FOUND
        # ---------------------------------

        if not search_results:

            return {

                "hallucination_risk": "HIGH",

                "evidence_score": 0,

                "trusted_document": None,

                "reason":
                    "No trusted knowledge was found to verify the AI response."
            }


        # ---------------------------------
        # GET BEST TRUSTED DOCUMENT
        # ---------------------------------

        trusted_document = search_results[0]

        trusted_content = trusted_document[
            "content"
        ]


        # ---------------------------------
        # COMPARE AI RESPONSE WITH
        # TRUSTED KNOWLEDGE
        # ---------------------------------

        try:

            vectorizer = TfidfVectorizer(
                stop_words="english"
            )


            vectors = vectorizer.fit_transform(
                [
                    ai_response,
                    trusted_content
                ]
            )


            similarity = cosine_similarity(
                vectors[0],
                vectors[1]
            )[0][0]


            evidence_score = round(
                float(similarity) * 100,
                2
            )


        except Exception:

            evidence_score = 0


        # ---------------------------------
        # DETERMINE HALLUCINATION RISK
        # ---------------------------------

        if evidence_score >= 35:

            hallucination_risk = "LOW"

            reason = (
                "The AI response has strong similarity "
                "with trusted knowledge."
            )


        elif evidence_score >= 15:

            hallucination_risk = "MEDIUM"

            reason = (
                "The AI response has partial support "
                "from trusted knowledge."
            )


        else:

            hallucination_risk = "HIGH"

            reason = (
                "The AI response has weak support "
                "from trusted knowledge."
            )


        # ---------------------------------
        # RETURN RESULT
        # ---------------------------------

        return {

            "hallucination_risk":
                hallucination_risk,

            "evidence_score":
                evidence_score,

            "trusted_document":
                trusted_document[
                    "document"
                ],

            "reason":
                reason
        }