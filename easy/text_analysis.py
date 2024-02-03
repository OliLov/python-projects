"""Text analysis."""

# pylint: disable=unspecified-encoding
import argparse


def count_words(file_path: str) -> int:
    """Count words in a file.

    :param file_path: The path to the file to count words for.
    :return: The number of words in the file.
    """
    with open(file_path, "r") as file:
        contents = file.read()
        words = contents.split()
        return len(words)


def count_characters(file_path: str) -> int:
    """Count characters in a file.

    :param file_path: The path to the file to count characters for.
    :return: The number of characters in the file.
    """
    with open(file_path, "r") as file:
        contents = file.read()
        return len(contents)


def main(file_path: str) -> None:
    """Word and character counter main function.

    :param file_path: The path to the file to count words and characters for.
    """
    word_count = count_words(file_path)
    character_count = count_characters(file_path)
    print(f"The file has {word_count} words and {character_count} characters.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Word and Character Counter")
    parser.add_argument("file_path", type=str, help="Path to the text file")
    args = parser.parse_args()

    main(args.file_path)
