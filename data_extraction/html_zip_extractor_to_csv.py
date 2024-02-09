"""Create CSV.

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
    titles = []
    with ZipFile(zip_file_path, "r") as zip_ref:
        # Extract zip to a temporary directory
        temp_dir = Path(zip_file_path.parent, "temp_extracted")
        zip_ref.extractall(temp_dir)

        # Identify HTML files within the extracted structure
        for file_path in temp_dir.rglob("*.html"):
            # Extract title from the filename using pathlib operations
            titles.append(file_path.name)

        # Cleanup extracted files
        shutil.rmtree(temp_dir)

    return titles


def create_csv_file(titles: list[str], csv_file_path: str) -> None:
    """Create a CSV file with the given titles.

    :param titles: The titles to include in the CSV file.
    :param csv_file_path: Path to the CSV output file.
    """
    with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["File", "Views", "Reads"])  # Write the header row
        for title in titles:
            writer.writerow([title, "0", "0"])  # Write each title


def main(zip_file_path: Path) -> None:
    """Main function for creating the CSV.

    :param zip_file_path: Path to the zip file containing HTML files.
    """
    csv_file_name = zip_file_path.stem + ".csv"
    csv_file_path = zip_file_path.parent.joinpath(csv_file_name)

    titles = extract_file_names(zip_file_path)
    if titles:
        create_csv_file(titles, csv_file_path)
        print(f"CSV file created successfully at {csv_file_path}")
    else:
        print("No titles were extracted.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Extract titles from HTML files in a zip archive and save to a "
            "CSV file."
        )
    )
    parser.add_argument(
        "zip_file_path", help="Path to the zip file containing HTML files."
    )

    args = parser.parse_args()
    main(Path(args.zip_file_path))
