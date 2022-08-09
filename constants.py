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

# Set the mapping for plot legend labels
SOFT = mpatches.Patch(color='red', label='Soft')
MEDIUM = mpatches.Patch(color='yellow', label='Medium')
HARD = mpatches.Patch(color='white', label='Hard')
INTERMEDIATE = mpatches.Patch(color='green', label='Intermediate')
WET = mpatches.Patch(color='blue', label='Wet')
TYRES_COLOR_LEGEND = [SOFT, MEDIUM, HARD, INTERMEDIATE, WET]

# Another color mapping... just for the purpose of line plot
TYRES_COLOR_DICT = {"SOFT": "red", "MEDIUM": "#FFC000", "HARD": "white", "INTERMEDIATE": "green",
                 "WET": "blue"}
