"""Chatbot interface for interacting with the creditworthiness system."""


def get_user_query() -> str:
    """Simulate getting a query from the user."""
    return input("Enter your question: ")


if __name__ == "__main__":
    query = get_user_query()
    print(f"You asked: {query}")
