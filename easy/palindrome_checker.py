"""Palindrome checker."""
import argparse


def is_palindrome(phrase: str, advanced: bool) -> bool:
    """Check if phrase is a palindrome.

    :param phrase: The phrase to check if it is a palindrome.
    :param advanced: If `True`,
        remove non-alphanumeric characters and convert to lowercase.
    :return: `True` if the phrase is a palindrome.
    """
    if advanced:
        # Remove non-alphanumeric characters and convert to lowercase.
        phrase = "".join(char.lower() for char in phrase if char.isalnum())
    return phrase == phrase[::-1]


def main(phrase: str, advanced: bool) -> None:
    """Palindrome checker main function.

    :param phrase: The phrase to check if it is a palindrome.
    :param advanced: If `True`,
        remove non-alphanumeric characters and convert to lowercase.
    """
    if is_palindrome(phrase, advanced):
        print(f"The phrase {phrase} is a palindrome.")
    else:
        print(f"The phrase {phrase} is NOT a palindrome.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Palidrome checker.")

    PHRASE_HELP = "The phrase to check if it is a palindrome"
    parser.add_argument("phrase", type=str, help=PHRASE_HELP)

    ADVANCED_HELP = "Enable advanced checking (ignores spaces, punctuation, and case)"
    parser.add_argument("-a", "--advanced", action="store_true", help=ADVANCED_HELP)

    args = parser.parse_args()
    main(args.phrase, args.advanced)
