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
from race import convert_laptime_to_seconds, get_all_driver_names
ff1.Cache.enable_cache('cache')


def remove_outlier_laps(df):
    df.loc[(np.abs(stats.zscore(df.LapTime)) >= 1), "LapTime"] = np.NaN


def get_tyre_model(df):
    # Plot a best fit line
    # Only consider the indices where both x and y are not missing
    valid_indices = np.isfinite(df.TyreLife) & np.isfinite(df.LapTime)

    # Only returns a model if valid
    # i.e. expect a non-empty vector for x
    if valid_indices.size > 0:
        return np.poly1d(np.polyfit(df.TyreLife[valid_indices], df.LapTime[valid_indices],
                                    TYRE_DEGRADATION_REGRESSION_DEGREE))

    return None


def plot_tyre_model(df, model=None, axes=None, row=0, column=0):
    # Get the range of the regression line wanted
    m = df.TyreLife.min()
    M = df.TyreLife.max()
    # The third parameter is the number of samples, set it to double of the laps
    polyline = np.linspace(m, M, int((M - m) * 2))

    if axes is not None:
        subplot = df.plot(kind='scatter', x='TyreLife', y='LapTime',
                          title=df['Driver'].unique().tolist()[0], ax=axes[row, column],
                          figsize=(25, 18))
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


def plot_tyre_model_all_drivers(df, tyre):
    # Make a subplot
    fig, axs = plt.subplots(5, 4)
    fig.subplots_adjust(hspace=0.4)
    fig.suptitle('Long Run Race Pace (' + tyre.capitalize() + ' Tires)')

    drivers = get_all_driver_names(df)
    for i in range(len(drivers)):
        # Only pick representative laps - laps that are set under green flag and not in/out laps
        fp2_representative_laps = df.pick_driver(
            drivers[i]).pick_accurate().pick_wo_box().pick_track_status('1')

        # Convert laptime from timedelta to seconds for plotting
        convert_laptime_to_seconds(fp2_representative_laps)

        # Consider only medium
        fp2_representative_laps_medium = fp2_representative_laps.pick_tyre(MEDIUM)

        remove_outlier_laps(fp2_representative_laps_medium)

        model = get_tyre_model(fp2_representative_laps_medium)
        if (fp2_representative_laps_medium.shape[0] > 0):
            plot_tyre_model(fp2_representative_laps_medium, model, axs, i // 4, i % 4)
        else:
            axs[i // 4, i % 4].title.set_text(drivers[i])
