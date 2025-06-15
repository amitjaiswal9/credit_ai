"""Entry point for the creditworthiness assessment application."""

from integrations.cibil_api import fetch_cibil_score
from integrations.iris_api import get_kyc_details
from rule_engine.policy_rules import is_eligible
from utils.logging_utils import configure_logging


def main(customer_id: str) -> None:
    configure_logging()
    score = fetch_cibil_score(customer_id)
    kyc = get_kyc_details(customer_id)
    if is_eligible(score, kyc.get("status", "")):
        print(f"Customer {customer_id} is eligible with score {score} and KYC {kyc['status']}.")
    else:
        print(f"Customer {customer_id} is not eligible with score {score} and KYC {kyc['status']}.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python app.py <customer_id>")
    main(sys.argv[1])
