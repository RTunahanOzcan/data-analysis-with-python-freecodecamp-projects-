import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
# Load data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data", alpha=0.6)

    # Line of best fit using all data
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_all = np.arange(df["Year"].min(), 2051)
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    plt.plot(x_pred_all, y_pred_all, 'r', label="Best fit: all data")

    # Line of best fit using data from 2000 onward
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_pred_2000 = np.arange(2000, 2051)
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, 'g', label="Best fit: 2000–present")

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()