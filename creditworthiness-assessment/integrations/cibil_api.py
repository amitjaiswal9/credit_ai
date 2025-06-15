"""Mock integration with CIBIL score provider."""

from random import randint


def fetch_cibil_score(customer_id: str) -> int:
    """Return a simulated CIBIL score for the given customer."""
    # In a real implementation, this would call an external API
    return randint(650, 800)
