"""
Contains helper functions for analysing qualifying data in notebook.
"""
import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from constants import *
import matplotlib.patches as mpatches
# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache')


def get_fastest_lap_in_qualifying(df):
    for q in QUALIFYING_SESSIONS:
        df.loc[:, q] = df[q].dt.total_seconds()
        df[q] = df[q].fillna(10000)

    times_df = pd.DataFrame(df.Abbreviation)

    for q in QUALIFYING_SESSIONS:
        times_df = pd.concat([times_df, df[q]], axis=1)

    times_df['Fastest Lap'] = times_df[QUALIFYING_SESSIONS].min(axis=1)

    return times_df
