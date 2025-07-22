# cli_tool.py
import argparse
from analyzer import evaluate_password

def main():
    parser = argparse.ArgumentParser(description="Check the strength of a password.")
    parser.add_argument("--password", required=True, help="Password to evaluate")
    args = parser.parse_args()

    result = evaluate_password(args.password)

    print(f"Rating: {result['rating']} (Score: {result['score']}/100)")
    print(f"Entropy: {result['entropy']} bits")
    if result['feedback']:
        print("Feedback:")
        for fb in result['feedback']:
            print(f"- {fb}")

if __name__ == "__main__":
    main()