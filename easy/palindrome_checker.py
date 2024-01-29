"""Palindrome checker."""
import argparse


def is_palindrome(phrase: str) -> bool:
    """Check if phrase is a palindrome.

    :param phrase: The pharse to check if it is a palindrome.
    :return: `True` if the phrase is a palindrome.
    """
    return phrase == phrase[::-1]


def main(phrase: str) -> None:
    """Palindrome checker main function.

    :param phrase: The pharse to check if it is a palindrome.
    """
    if is_palindrome(phrase):
        print(f"The phrase {phrase} is a palindrome.")
    else:
        print(f"The phrase {phrase} is NOT a palindrome.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Palidrome checker.")

    PHRASE_HELP = "The phrase to check if it is a palindrome"
    parser.add_argument("phrase", type=str, help=PHRASE_HELP)

    args = parser.parse_args()
    main(args.phrase)
