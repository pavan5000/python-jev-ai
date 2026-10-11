import argparse
import os

from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient


load_dotenv()

DEFAULT_STATE = (
    "I've been unable to access my account all morning, and I need this fixed "
    "before my meeting in an hour."
)


def evaluate_urgency(state: str) -> float:
    api_key = os.environ.get("TYPESAFE_API_KEY")
    if not api_key:
        raise RuntimeError("Set the TYPESAFE_API_KEY environment variable before running.")

    with TypeSafeClient(
        api_key=api_key,
        base_url="https://api.typesafe.ai",
        model="jev-latest",
    ) as client:
        response = client.system_one(
            state=state,
            questions={
                "urgency": Noul(
                    instructions="Does this message express urgency or time-sensitivity?"
                )
            },
        )
    print(response)
    return response.nouls["urgency"].noul


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate how urgent a message is with TypeSafe Jev."
    )
    parser.add_argument(
        "state",
        nargs="?",
        default=DEFAULT_STATE,
        help="Text for Jev to evaluate (defaults to a sample message).",
    )
    args = parser.parse_args()

    urgency = evaluate_urgency(args.state)
    print(f"Urgency: {urgency:.3f}")


if __name__ == "__main__":
    main()
