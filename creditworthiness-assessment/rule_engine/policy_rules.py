"""Business policy rules for credit decisions."""

THRESHOLD_SCORE = 700
VERIFIED_STATUS = "verified"


def is_eligible(cibil_score: int, kyc_status: str) -> bool:
    """Determine eligibility based on score and KYC status."""
    return cibil_score >= THRESHOLD_SCORE and kyc_status.lower() == VERIFIED_STATUS
