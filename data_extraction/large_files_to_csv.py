"""Large files to CSV.

Sorts large files by date into a CSV from a directory.
"""

import argparse
import csv
import re
from datetime import datetime
from pathlib import Path

from html_zip_extractor_to_csv import create_csv_file


def parse_date(file_name: str) -> datetime:
    """Parse the date from the beginning of a file name, assuming it's in
    'YYYY-MM-DD' format.

    :param file_name: The name of the file from which to extract the date.
    :return: A datetime object with the extracted date.
    """
    date_str = file_name.split("_")[0]
    return datetime.strptime(date_str, "%Y-%m-%d")


def sort_csv_entries(csv_file_path: Path) -> None:
    """Sorts entries in a CSV file by date.

    :param csv_file_path: The path to the CSV file to be sorted.
    """
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)
        entries = list(reader)

    sorted_entries = sorted(
        entries, key=lambda x: parse_date(x[0]), reverse=True
    )

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(sorted_entries)


def is_date_prefixed(file_name: str) -> bool:
    """Determines if a file name starts with a date in 'YYYY-MM-DD' format.

    :param file_name: The name of the file to check.
    :return: `True` if the file name starts with a date, otherwise `False`.
    """
    date_pattern = r"^\d{4}-\d{2}-\d{2}_"
    return bool(re.match(date_pattern, file_name))


def list_large_files(
    directory_path: Path, size_threshold_kb: int = 5
) -> list[str]:
    """Lists file names in a given directory that exceed the specified size
    threshold and are prefixed with a date.

    :param directory_path: Path to the directory to search.
    :param size_threshold_kb: Size threshold in kilobytes.
    :return: A list of file names that are larger than the specified size.
    """
    size_threshold_bytes = size_threshold_kb * 1024

    large_files = []
    for file_path in directory_path.iterdir():
        if (
            file_path.is_file()
            and file_path.stat().st_size > size_threshold_bytes
            and is_date_prefixed(file_path.name)
        ):
            large_files.append(file_path.name)

    return large_files


def main(directory_path: Path) -> None:
    """Main function to list large files in a directory, write them to a CSV,
    and sort this CSV by date.

    :param directory_path: Path to the directory.
    """
    csv_file_name = directory_path.name + "_large_files.csv"
    csv_file_path = directory_path.parent.joinpath(csv_file_name)

    large_file_names = list_large_files(directory_path)
    create_csv_file(large_file_names, csv_file_path)
    print(f"CSV file created successfully at {csv_file_path}")

    sort_csv_entries(csv_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Extract and list names of large files in a directory to a CSV "
            "file, then sort the file by date."
        )
    )
    parser.add_argument(
        "directory_path",
        type=str,
        help="Path to the directory to search for large files.",
    )

    args = parser.parse_args()
    main(Path(args.directory_path))
