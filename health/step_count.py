"""Step count."""

import argparse
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def find_longest_streak(
    daily_steps: dict[datetime, int], steps: int
) -> tuple[Optional[datetime], int]:
    """Find the longest streak of steps.

    A streak is defined as consecutive days meeting the specified step count.

    :param daily_steps: Dictionary with the dates and respective step count.
    :param steps: Number of steps to find the longest streak for.
    :return: Longest streak start date and total number of days.
    """
    sorted_dates = sorted(daily_steps.keys())

    longest_streak = 0
    current_streak = 0
    longest_streak_start_date = None
    current_streak_start_date = None

    for idx, date in enumerate(sorted_dates):
        # Check if the steps on the current date meet or exceed the target.
        if daily_steps[date] >= steps:
            # Increment the current streak.
            current_streak += 1
            # Set the start date of the current streak.
            if current_streak_start_date is None:
                current_streak_start_date = date
        else:
            # If the current day does not meet the step target, then check if
            # the current streak is the longest one update the longest streak.
            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_streak_start_date = current_streak_start_date
            # Reset the current streak variables for the next possible streak.
            current_streak = 0
            current_streak_start_date = None

        # Check if the last streak was the longest.
        if idx == len(sorted_dates) - 1 and current_streak > longest_streak:
            longest_streak = current_streak
            longest_streak_start_date = current_streak_start_date

    return longest_streak_start_date, longest_streak


def day_with_most_steps(
    daily_steps: defaultdict[datetime, int]
) -> tuple[datetime, int]:
    """Find the day with the most steps.

    :param daily_steps: Dicionary with the dates and respective step count.
    :return: Day with most steps and respetive step count.
    """
    max_daily_steps = max(list(daily_steps.values()))
    max_daily_steps_idx = list(daily_steps.values()).index(max_daily_steps)

    return list(daily_steps)[max_daily_steps_idx], max_daily_steps


def plot_guideline(guideline: int, axis: str):
    """Overlay a guideline on the current plot.

    :param guideline: Guideline value for number of steps.
    :param axis: Axis for the guideline ('x' or 'y').
    """
    if axis == "y":
        plt.axhline(
            y=guideline,
            color="black",
            linestyle="--",
            label=f"Guideline: {guideline} steps",
        )
    elif axis == "x":
        plt.axvline(
            x=guideline,
            color="black",
            linestyle="--",
            label=f"Guideline: {guideline} steps",
        )
    else:
        raise ValueError("Invalid axis argument. Use 'x' or 'y'.")

    plt.legend()


def plot_cumulative_steps(daily_steps: defaultdict[datetime, int]) -> None:
    """Plot cumulative step count.

    :param daily_steps: Dictionary with the dates and respective step count.
    """
    dates = []
    cumulative_steps = []
    total_steps = 0

    sorted_dates = sorted(list(daily_steps.keys()))
    for date in sorted_dates:
        total_steps += daily_steps[date]
        cumulative_steps.append(total_steps)
        dates.append(date)

    plt.figure(figsize=(10, 6))
    plt.plot(dates, cumulative_steps, linestyle="-", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Step Count")
    plt.title("Cumulative Daily Step Count")
    plt.xticks(rotation=45)
    plt.tight_layout()


def plot_average_steps_per_weekday(
    daily_steps: defaultdict[datetime, int]
) -> None:
    """Plot average steps per weekday.

    :param daily_steps: Dictionary with the dates and respective step count.
    """
    weekday_steps = defaultdict(list)

    for date, steps in daily_steps.items():
        weekday = date.weekday()
        weekday_steps[weekday].append(steps)

    average_steps_per_weekday = {
        weekday: np.mean(steps) for weekday, steps in weekday_steps.items()
    }

    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    average_steps = [average_steps_per_weekday[i] for i in range(7)]

    plt.figure(figsize=(10, 6))
    plt.bar(weekdays, average_steps, color=colors)
    plt.xlabel("Day of the Week")
    plt.ylabel("Average Steps")
    plt.title("Average Steps per Weekday")
    plt.tight_layout()


def plot_daily_step_distribution(
    daily_steps: defaultdict[datetime, int]
) -> None:
    """Plot daily step count distribution.

    :param daily_steps: Dictionary with the dates and respective step count.
    """
    daily_step_totals = list(daily_steps.values())

    mean_daily_steps = np.mean(daily_step_totals)
    std_dev_daily_steps = np.std(daily_step_totals)

    min_daily_steps = min(daily_step_totals)
    max_daily_steps = max(daily_step_totals)

    # pylint: disable=invalid-name
    x = np.linspace(min_daily_steps, max_daily_steps, 100)
    y = stats.norm.pdf(x, mean_daily_steps, std_dev_daily_steps)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, "b-", linewidth=2)
    plt.title("Daily Step Count Distribution")
    plt.xlabel("Daily Step Count")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.xlim(min_daily_steps, max_daily_steps)


def load_data(file_path: str) -> defaultdict[datetime, int]:
    """Load data.

    :param file_path: File path to health data.
    :return: Dictionary with the dates and respective step count.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()

    daily_steps = defaultdict(int)

    records = root.findall(
        ".//Record[@type='HKQuantityTypeIdentifierStepCount']"
    )
    for record in records:
        start_date = record.get("startDate")
        value = int(record.get("value"))
        date_obj = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S %z").date()
        daily_steps[date_obj] += value

    return daily_steps


def main(
    file_path: str,
    metrics: list[str],
    steps: Optional[int],
    guideline: Optional[int],
) -> None:
    """Main function.

    :param file_path: File path to health data.
    :param metrics: Optional parameter for metrics to display.
    :param steps: Optional parameter for calculating the longest streak.
    :param guideline: Optional parameter for inserting guideline.
    """
    daily_steps = load_data(file_path)

    most_steps_date, most_steps_count = day_with_most_steps(daily_steps)
    print(
        (
            f"The day with the most steps is "
            f"{most_steps_date.strftime('%Y-%m-%d')} with "
            f"{most_steps_count} steps."
        )
    )

    if not metrics or "cumulative" in metrics:
        plot_cumulative_steps(daily_steps)
        plt.show()

    if not metrics or "weekday" in metrics:
        plot_average_steps_per_weekday(daily_steps)
        if guideline is not None:
            plot_guideline(guideline, "y")
        plt.show()

    if not metrics or "distribution" in metrics:
        plot_daily_step_distribution(daily_steps)
        if guideline is not None:
            plot_guideline(guideline, "x")
        plt.show()

    if (not metrics or "streak" in metrics) and steps is not None:
        longest_streak_start, longest_streak_length = find_longest_streak(
            daily_steps, steps
        )
        print(
            (
                f"The longest streak of at least {steps} steps is "
                f"{longest_streak_length} days, starting on "
                f"{longest_streak_start}."
            )
        )
    elif not metrics or "streak" in metrics:
        raise ValueError(
            "When using the 'streak' metric, you must also specify --steps"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze health data for step count metrics."
    )

    FILE_PATH_HELP = "The file path to the export.xml file"
    parser.add_argument("file_path", type=str, help=FILE_PATH_HELP)

    METRICS_HELP = (
        "Specify one or more health metrics: cumulative, weekday, "
        "distribution, streak"
    )
    parser.add_argument(
        "-m",
        "--metrics",
        nargs="+",
        help=METRICS_HELP,
    )

    STEPS_HELP = (
        "Specify the minimum number of steps for calculating the longest "
        "streak"
    )
    parser.add_argument(
        "-s",
        "--steps",
        type=int,
        help=STEPS_HELP,
    )

    GUIDELINE_HELP = "Specify the guideline for the number of steps per day"
    parser.add_argument(
        "-g",
        "--guideline",
        type=int,
        help=GUIDELINE_HELP,
    )

    args = parser.parse_args()
    main(args.file_path, args.metrics, args.steps, args.guideline)
