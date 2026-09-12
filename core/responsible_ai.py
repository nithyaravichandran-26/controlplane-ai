import re


class ResponsibleAIEngine:

    def __init__(self):
        self.toxic_words = [
            "idiot",
            "stupid",
            "useless",
            "hate",
            "kill",
            "shut up"
        ]

        self.bias_patterns = [
            "because she is a woman",
            "because he is a man",
            "because of their religion",
            "because of their race",
            "because of their caste",
            "people of that race",
            "people of that religion"
        ]

        self.policy_violations = [
            "guaranteed refund",
            "guarantee a refund",
            "share your password",
            "give me your password",
            "reveal confidential information",
            "ignore company policy"
        ]

    def detect_pii(self, text):
        findings = []

        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        phone_pattern = r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b"

        if re.search(email_pattern, text):
            findings.append("Email address detected")

        if re.search(phone_pattern, text):
            findings.append("Phone number detected")

        return findings

    def detect_toxicity(self, text):
        text_lower = text.lower()

        findings = []

        for word in self.toxic_words:
            if word in text_lower:
                findings.append(word)

        return findings

    def detect_bias(self, text):
        text_lower = text.lower()

        findings = []

        for pattern in self.bias_patterns:
            if pattern in text_lower:
                findings.append(pattern)

        return findings

    def detect_policy_violation(self, text):
        text_lower = text.lower()

        findings = []

        for pattern in self.policy_violations:
            if pattern in text_lower:
                findings.append(pattern)

        return findings

    def analyze(self, text):

        pii_findings = self.detect_pii(text)

        toxicity_findings = self.detect_toxicity(text)

        bias_findings = self.detect_bias(text)

        policy_findings = self.detect_policy_violation(text)

        total_issues = (
            len(pii_findings)
            + len(toxicity_findings)
            + len(bias_findings)
            + len(policy_findings)
        )

        if total_issues == 0:
            risk_level = "LOW"

        elif total_issues <= 2:
            risk_level = "MEDIUM"

        else:
            risk_level = "HIGH"

        return {
            "pii_detected": len(pii_findings) > 0,
            "pii_findings": pii_findings,

            "toxicity_detected": len(toxicity_findings) > 0,
            "toxicity_findings": toxicity_findings,

            "bias_detected": len(bias_findings) > 0,
            "bias_findings": bias_findings,

            "policy_violation_detected": len(policy_findings) > 0,
            "policy_findings": policy_findings,

            "total_issues": total_issues,
            "risk_level": risk_level
        }