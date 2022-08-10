"""
Contains helper functions for analysing race data in notebook.
"""
import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from constants import *
from scipy import stats
import matplotlib.patches as mpatches
# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache')


def remove_outlier_laps(df):
    df.loc[(np.abs(stats.zscore(df.LapTime)) >= 1), "LapTime"] = np.NaN


def get_tyre_model(df):
    # Plot a best fit line
    # Only consider the indices where both x and y are not missing
    valid_indices = np.isfinite(df.TyreLife) & np.isfinite(df.LapTime)
    model = np.poly1d(np.polyfit(df.TyreLife[valid_indices], df.LapTime[valid_indices],
                                 TYRE_DEGRADATION_REGRESSION_DEGREE))

    return model


def plot_tyre_model(df, model=None, axes=None, row=0, column=0):
    # Get the range of the regression line wanted
    m = df.TyreLife.min()
    M = df.TyreLife.max()
    # The third parameter is the number of samples, set it to double of the laps
    polyline = np.linspace(m, M, int((M - m) * 2))

    if axes is not None:
        subplot = df.plot(kind='scatter', x='TyreLife', y='LapTime',
                          title=df['Driver'].unique().tolist()[0], ax=axes[row, column])
        # Plot the line
        if model is not None:
            axes[row, column].plot(polyline, model(polyline))
    else:
        subplot = df.plot(kind='scatter', x='TyreLife', y='LapTime',
                          title=df['Driver'].unique().tolist()[0])
        # Plot the line
        if model is not None:
            plt.plot(polyline, model(polyline))

    return subplot
