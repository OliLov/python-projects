"""Medium Statistics Plots.

Provides visualization of Medium post statistics.
"""

from itertools import cycle
from typing import Any

import matplotlib.pyplot as plt
import mplcursors
import mplcyberpunk
import numpy as np
import pandas as pd
import seaborn as sns

color_cycle = cycle(["#00ffd0", "#ff00ab", "#ffae00", "#00ff15", "#00c3ff"])


class MediumStatisticsPlotter:
    """Medium statistics plotter."""

    def __init__(self, analyses: list[dict[str, Any]]) -> None:
        """Initalize the Medium statistics plotter.

        :param analyses: A list of dictionaries, each entry containing analysis
            results for a single Medium post.
        """
        self.data = pd.DataFrame(
            {
                "Content Length": [a["content_length"] for a in analyses],
                "Readability Score": [
                    a["readability_score"] for a in analyses
                ],
                "Sentiment Score": [a["sentiment_score"] for a in analyses],
                "Title Length": [a["title_length"] for a in analyses],
                "Reads": [a["reads"] for a in analyses],
                "Views": [a["views"] for a in analyses],
                "Read-to-View Ratio": [
                    a["reads"] / a["views"] if a["views"] else 0
                    for a in analyses
                ],
                "Weekday": [a["date"].weekday() for a in analyses],
                "Titles": [a["title"] for a in analyses],
            }
        )

        # Customize seaborn theme.
        plt.style.use("cyberpunk")
        sns.set_palette("mako")

    def __plot_distributions(
        self, column: str, title: str, xlabel: str
    ) -> None:
        """Plots the distribution of a specified metric.

        :param column: The name of the DataFrame column to plot.
        :param title: The title of the plot.
        :param xlabel: The label for the x-axis.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], bins=20, color="skyblue", kde=True)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel("Number of posts")

        mplcyberpunk.add_glow_effects()
        plt.show()

    # pylint: disable=too-many-arguments
    def __plot_correlation(
        self, x_name: str, y_name: str, xlabel: str, ylabel: str, title: str
    ) -> None:
        """Plots and annotates the correlation between two variables.

        :param x_name: The column name for the x-axis.
        :param y_name: The column name for the y-axis.
        :param xlabel: Label for the x-axis.
        :param ylabel: Label for the y-axis.
        :param title: The title of the plot.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_name, y=y_name, data=self.data)

        corr = np.corrcoef(self.data[x_name], self.data[y_name])[0, 1]
        slope, intercept = np.polyfit(self.data[x_name], self.data[y_name], 1)

        line_x = np.linspace(
            self.data[x_name].min(), self.data[x_name].max(), 100
        )
        line_y = slope * line_x + intercept

        plt.plot(line_x, line_y, color=next(color_cycle))
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.annotate(
            f"Correlation: {corr:.2f}",
            xy=(0.05, 0.95),
            xycoords="axes fraction",
            ha="left",
            va="center",
            fontsize=12,
            color="white",
            bbox={
                "boxstyle": "round,pad=0.5",
                "fc": "black",
                "ec": "none",
                "alpha": 0.5,
            },
        )

        mplcyberpunk.make_lines_glow()
        cursor = mplcursors.cursor(hover=True)
        cursor.connect(
            "add",
            lambda sel: sel.annotation.set_text(
                self.data.iloc[sel.index]["Titles"]
            ),
        )
        cursor.connect(
            "add",
            lambda sel: sel.annotation.get_bbox_patch().set(
                fc="black", alpha=0.7
            ),
        )

        plt.tight_layout()
        plt.show()

    def plot_reads_distribution(self) -> None:
        """Plots the distribution of reads across Medium posts."""
        self.__plot_distributions("Reads", "Distribution of reads", "Reads")

    def plot_views_distribution(self) -> None:
        """Plots the distribution of views across Medium posts."""
        self.__plot_distributions("Views", "Distribution of views", "Views")

    def plot_reads_to_views(self) -> None:
        """Plots the reads to views ratio"""
        plt.figure(figsize=(12, 8))

        read_view_ratio = self.data["Read-to-View Ratio"]
        self.data["Color"] = read_view_ratio.apply(
            lambda x: "lime" if x > 0.5 else "red"
        )

        sns.scatterplot(
            x="Views",
            y="Reads",
            hue="Color",
            data=self.data,
            palette=["red", "lime"],
            legend=False,
        )

        plt.title("Reads to views")
        plt.xlabel("Views")
        plt.ylabel("Reads")

        average_ratio = read_view_ratio.mean()
        plt.annotate(
            f"Average read-to-view ratio: {average_ratio:.2f}",
            xy=(0.05, 0.95),
            xycoords="axes fraction",
            ha="left",
            va="center",
            fontsize=12,
            color="white",
            bbox={
                "boxstyle": "round,pad=0.5",
                "fc": "black",
                "ec": "none",
                "alpha": 0.5,
            },
        )

        mplcursors.cursor(hover=True).connect(
            "add",
            lambda sel: sel.annotation.set_text(
                self.data.iloc[sel.index]["Titles"]
            ),
        )

        plt.tight_layout()
        plt.show()

    def plot_correlation_between(
        self, attribute1: str, attribute2: str
    ) -> None:
        """Plots the correlation between two specified attributes.

        :param attribute1: The first attribute for comparison.
        :param attribute2: The second attribute for comparison.
        """
        self.__plot_correlation(
            attribute1,
            attribute2,
            xlabel=attribute1,
            ylabel=attribute2,
            title=f"{attribute1} vs. {attribute2}",
        )

    def plot_weekday_reads_correlation(self) -> None:
        """Average reads and the weekday of publishing correlation."""
        plt.figure(figsize=(10, 6))

        day_names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        self.data["Weekday Name"] = self.data["Weekday"].apply(
            lambda x: day_names[x]
        )

        weekday_reads_avg = (
            self.data.groupby("Weekday Name")["Reads"]
            .mean()
            .reindex(day_names)
        )

        sns.barplot(
            x=weekday_reads_avg.index,
            y=weekday_reads_avg.values,
            palette=color_cycle,
        )

        plt.title("Average reads by weekday")
        plt.xlabel("Weekday")
        plt.ylabel("Average reads")
        plt.xticks(rotation=45)

        mplcyberpunk.add_glow_effects()

        plt.tight_layout()
        plt.show()
