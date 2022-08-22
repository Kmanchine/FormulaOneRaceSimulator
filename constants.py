"""
Contains constants for analysing a Fomrula 1 weekend.
"""
import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache')

# Constants for tyre strings
SOFT = 'SOFT'
MEDIUM = 'MEDIUM'
HARD = 'HARD'
INTERMEDIATE = 'INTERMEDIATE'
WET = 'WET'
DRY_TYRES = [SOFT, MEDIUM, HARD]
WET_TYRES = [INTERMEDIATE, WET]

# Set the mapping for plot legend labels
SOFT_PATCHES = mpatches.Patch(color='red', label='Soft')
MEDIUM_PATCHES = mpatches.Patch(color='yellow', label='Medium')
HARD_PATCHES = mpatches.Patch(color='white', label='Hard')
INTERMEDIATE_PATCHES = mpatches.Patch(color='green', label='Intermediate')
WET_PATCHES = mpatches.Patch(color='blue', label='Wet')
TYRES_COLOR_LEGEND = [SOFT_PATCHES, MEDIUM_PATCHES, HARD_PATCHES, INTERMEDIATE_PATCHES, WET_PATCHES]

# Another color mapping... just for the purpose of line plot
TYRES_COLOR_DICT = {"SOFT": "red", "MEDIUM": "#FFC000", "HARD": "white", "INTERMEDIATE": "green",
                 "WET": "blue"}

TYRE_DEGRADATION_REGRESSION_DEGREE = 2

QUALIFYING_SESSIONS = ['Q1', 'Q2', 'Q3']
