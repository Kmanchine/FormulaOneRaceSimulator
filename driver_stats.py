import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from race import *
from race_sim import *
from qualifying import *
from constants import *
from practice import *
from scipy import stats
from scipy.optimize import curve_fit


def get_stint_lengths(stints_list: list):
    if stints_list == []:
        return []

    stints_tuples = []
    stint_laps = 0
    curr = None
    for i in range(len(stints_list)):
        curr = stints_list[i]
        if i == 0:
            stint_laps = 1
        else:
            stint_laps += 1
            prev = stints_list[i - 1]
            if curr != prev:
                stints_tuples.append((prev, stint_laps - 1))
                stint_laps = 1

    stints_tuples.append((curr, stint_laps))
    return stints_tuples
