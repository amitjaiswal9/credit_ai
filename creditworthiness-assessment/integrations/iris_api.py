"""Mock integration with IRIS KYC service."""

from random import choice

STATUSES = ["verified", "pending", "rejected"]


def get_kyc_details(customer_id: str) -> dict:
    """Return mock KYC details for the given customer."""
    # In reality, this would call the IRIS API
    return {"customer_id": customer_id, "status": choice(STATUSES)}
