"""Medium Post Analysis Script.

This script provides a comprehensive analysis of Medium posts, leveraging both
the content of the posts and their reads and view. It processes a directory of
HTML files representing individual Medium stories and a CSV file that contains
performance statistics for each story. For each post, the script extracts and
calculates various metrics, including the publishing date, content length,
sentiment score, title length, readability score, views, and reads. These
metrics are then analyzed to identify correlations between content
characteristics and reader engagement.

The script will output a series of plots illustrating various aspects of the
data, such as the distribution of reads and views, and correlations between
post characteristics and engagement metrics.

Key Features:
- Extraction of the publishing date and title from the file name.
- Extraction of views and reads data from an accompanying CSV file.
- Calculation of content length, sentiment score, title length, and readability
  score from the post's text.
- Generation of plots to visualize the distribution of reads and views, the
  relationship between different metrics and reader engagement, and the
  correlation of post characteristics with reads.

Usage:
1. Export Medium posts.
2. Prepare a CSV file with columns for the file name
   (matching those in the directory), views, and reads for each post.
3. Run the script with the path to the directory and the CSV file as arguments.
"""

# pylint: disable=no-member
import argparse
from datetime import datetime
from pathlib import Path
from pprint import pprint
from typing import Any

import nltk
import pandas as pd
import textstat
from bs4 import BeautifulSoup
from medium_statistics_plots import MediumStatisticsPlotter
from nltk.sentiment import SentimentIntensityAnalyzer


def extract_title_and_date(file_name: str) -> tuple[str, datetime]:
    """Extracts the title and date from a file name.

    This function parses the file name, which is expected to follow a specific
    format where the date precedes the title, separated by underscores. The
    date is expected to be in the "YYYY-MM-DD" format.

    :param file_name: The name of file to extract the title and date.
    :return: A tuple containing the title of the post and the publishing date.
    """
    parts = file_name.split("_")

    date_str = parts[0] if len(parts) > 0 else None
    date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else None

    title_part = "_".join(parts[1:])
    title = (
        title_part.replace("--", " ").replace("-", " ")
        if len(parts) > 1
        else None
    )

    title = title.rsplit("-", 1)[0] if title else title
    title = title.rsplit(".", 1)[0] if title else title

    return title, date


# pylint: disable=too-many-locals
def analyze_posts(
    posts_directory: Path, csv_path: Path
) -> list[dict[str, Any]]:
    """Analyze posts in a given directory against statistics in a CSV file.

    :param posts_directory: Path to the directory containing post files.
    :param csv_path: Path to the CSV file with post statistics.
    :return: A list of dictionaries with analysis results for each post.
    """
    medium_stats = pd.read_csv(csv_path)
    analyses = []
    stats_dict = {
        row["File"]: {"views": row["Views"], "reads": row["Reads"]}
        for _, row in medium_stats.iterrows()
    }
    sia = SentimentIntensityAnalyzer()

    for file_path in posts_directory.iterdir():
        file_name = file_path.name
        if file_name in stats_dict.keys():
            with open(file_path, "r", encoding="utf-8") as current_file:
                content = current_file.read()
                soup = BeautifulSoup(content, "html.parser")

                text = soup.get_text(separator=" ", strip=True)

                content_length = len(nltk.word_tokenize(text))
                sentiment_score = sia.polarity_scores(text)["compound"]
                title = soup.title.string if soup.title else ""
                title_length = len(nltk.word_tokenize(title))
                readability_score = textstat.flesch_reading_ease(text)

                views = stats_dict[file_name]["views"]
                reads = stats_dict[file_name]["reads"]

                title, date = extract_title_and_date(file_name)
                analyses.append(
                    {
                        "title": title,
                        "date": date,
                        "content_length": content_length,
                        "sentiment_score": sentiment_score,
                        "title_length": title_length,
                        "readability_score": readability_score,
                        "views": views,
                        "reads": reads,
                    }
                )
        else:
            print(f"File not found in CSV: {file_name}")

    return analyses


def main(posts_directory: Path, csv_path: Path) -> None:
    """Main function to execute the Medium post analysis.

    :param posts_directory: Path to the directory containing post files.
    :param csv_path: Path to the CSV file with post statistics.
    """
    analyses = analyze_posts(posts_directory, csv_path)

    pprint(analyses)
    medium_stats = MediumStatisticsPlotter(analyses)

    medium_stats.plot_reads_distribution()
    medium_stats.plot_views_distribution()
    medium_stats.plot_reads_to_views()
    medium_stats.plot_correlation_between("Content Length", "Reads")
    medium_stats.plot_correlation_between("Readability Score", "Reads")
    medium_stats.plot_correlation_between("Sentiment Score", "Reads")
    medium_stats.plot_correlation_between("Title Length", "Reads")
    medium_stats.plot_weekday_reads_correlation()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze Medium posts from a directory and CSV"
    )
    parser.add_argument(
        "posts_directory", type=str, help="Directory path to the posts"
    )
    parser.add_argument(
        "csv_path", type=str, help="Path to the CSV file with post statistics"
    )

    args = parser.parse_args()

    main(Path(args.posts_directory), Path(args.csv_path))
