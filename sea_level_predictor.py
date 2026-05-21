from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    csv_path = Path(__file__).with_name("epa-sea-level.csv")
    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_all = np.arange(df["Year"].min(), 2051)
    result_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    ax.plot(
        years_all,
        result_all.intercept + result_all.slope * years_all,
        color="red"
    )

    df_recent = df[df["Year"] >= 2000]
    years_recent = np.arange(2000, 2051)
    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    ax.plot(
        years_recent,
        result_recent.intercept + result_recent.slope * years_recent,
        color="green"
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    plt.savefig("sea_level_plot.png")
    return ax