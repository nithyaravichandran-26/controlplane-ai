import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class KnowledgeBase:

    def __init__(self):

        current_file = os.path.abspath(__file__)

        core_folder = os.path.dirname(current_file)

        project_folder = os.path.dirname(core_folder)

        self.knowledge_base_path = os.path.join(
            project_folder,
            "data",
            "knowledge_base"
        )


    # ---------------------------------
    # LOAD KNOWLEDGE DOCUMENTS
    # ---------------------------------

    def load_documents(self):

        documents = []


        if not os.path.exists(
            self.knowledge_base_path
        ):

            return documents


        for filename in os.listdir(
            self.knowledge_base_path
        ):

            if filename.endswith(".txt"):

                file_path = os.path.join(
                    self.knowledge_base_path,
                    filename
                )


                try:

                    with open(
                        file_path,
                        "r",
                        encoding="utf-8"
                    ) as file:

                        content = file.read()


                        documents.append(
                            {
                                "document": filename,
                                "content": content
                            }
                        )


                except Exception:

                    pass


        return documents


    # ---------------------------------
    # SEARCH KNOWLEDGE BASE
    # ---------------------------------

    def search(
        self,
        user_query,
        top_k=1
    ):

        documents = self.load_documents()


        if not documents:

            return []


        contents = []


        for document in documents:

            contents.append(
                document["content"]
            )


        vectorizer = TfidfVectorizer(
            stop_words="english"
        )


        try:

            vectors = vectorizer.fit_transform(
                [user_query] + contents
            )


            query_vector = vectors[0]

            document_vectors = vectors[1:]


            similarities = cosine_similarity(
                query_vector,
                document_vectors
            )[0]


            results = []


            for index, similarity in enumerate(
                similarities
            ):

                results.append(
                    {
                        "document": documents[index][
                            "document"
                        ],

                        "content": documents[index][
                            "content"
                        ],

                        "similarity": round(
                            float(similarity) * 100,
                            2
                        )
                    }
                )


            results.sort(
                key=lambda x: x["similarity"],
                reverse=True
            )


            return results[:top_k]


        except Exception:

            return []


    # ---------------------------------
    # ANALYZE KNOWLEDGE GROUNDING
    # ---------------------------------

    def analyze(
        self,
        user_query,
        ai_response
    ):

        search_results = self.search(
            user_query,
            top_k=1
        )


        # ---------------------------------
        # NO KNOWLEDGE FOUND
        # ---------------------------------

        if not search_results:

            return {

                "knowledge_risk": "HIGH",

                "knowledge_status":
                    "NOT AVAILABLE",

                "trusted_document": None,

                "document_similarity": 0,

                "evidence_score": 0,

                "message":
                    "No trusted knowledge document was found."
            }


        # ---------------------------------
        # GET BEST MATCHING DOCUMENT
        # ---------------------------------

        trusted_document = search_results[0]

        trusted_content = trusted_document[
            "content"
        ]

        document_similarity = trusted_document[
            "similarity"
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
        # DETERMINE KNOWLEDGE RISK
        # ---------------------------------

        if evidence_score >= 35:

            knowledge_risk = "LOW"

            knowledge_status = "GROUNDED"


        elif evidence_score >= 15:

            knowledge_risk = "MEDIUM"

            knowledge_status = (
                "PARTIALLY GROUNDED"
            )


        else:

            knowledge_risk = "HIGH"

            knowledge_status = (
                "NOT GROUNDED"
            )


        # ---------------------------------
        # RETURN RESULT
        # ---------------------------------

        return {

            "knowledge_risk":
                knowledge_risk,

            "knowledge_status":
                knowledge_status,

            "trusted_document":
                trusted_document["document"],

            "document_similarity":
                document_similarity,

            "evidence_score":
                evidence_score,

            "message":
                "Knowledge analysis completed."
        }