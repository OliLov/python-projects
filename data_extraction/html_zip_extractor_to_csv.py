"""HTML zip extractor to CSV.

Opens a zip file to extract the names of HTML files contained within.
It then creates a CSV file with the following format: [File name, Views, Reads]
"""

import argparse
import csv
import shutil
from pathlib import Path
from zipfile import ZipFile


def extract_file_names(zip_file_path: Path) -> list[str]:
    """Extract names of HTML files within the zip archive.

    :param zip_file_path: Path to zip file.
    :return: List of HTML file names.
    """
    file_names = []
    with ZipFile(zip_file_path, "r") as zip_ref:
        temp_dir = Path(zip_file_path.parent, "temp")
        zip_ref.extractall(temp_dir)

        for file_path in temp_dir.rglob("*.html"):
            file_names.append(file_path.name)

        shutil.rmtree(temp_dir)

    return file_names


def create_csv_file(file_names: list[str], csv_file_path: str) -> None:
    """Create a CSV file with the given file names.

    :param file_names: The file names to include in the CSV file.
    :param csv_file_path: Path to the CSV output file.
    """
    with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File", "Views", "Reads"])
        for file_name in file_names:
            writer.writerow([file_name, "0", "0"])


def main(zip_file_path: Path) -> None:
    """Main function for creating the CSV.

    :param zip_file_path: Path to the zip file containing HTML files.
    """
    csv_file_name = zip_file_path.stem + ".csv"
    csv_file_path = zip_file_path.parent.joinpath(csv_file_name)

    file_names = extract_file_names(zip_file_path)
    if file_names:
        create_csv_file(file_names, csv_file_path)
        print(f"CSV file created successfully at {csv_file_path}")
    else:
        print("No file names were extracted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Extract file name from HTML files in a zip archive and save to a "
            "CSV file."
        )
    )
    parser.add_argument(
        "zip_file_path", help="Path to the zip file containing HTML files."
    )

    args = parser.parse_args()
    main(Path(args.zip_file_path))
