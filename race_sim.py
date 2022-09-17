import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from race import *
from qualifying import *
from constants import *
from practice import *
from scipy import stats
from scipy.optimize import curve_fit

# Enable the cache by providing the name of the cache folder
ff1.Cache.enable_cache('cache')


def tyre_degradation_model(x, compound):
    if compound == SOFT:
        return 0.0025 * x ** 2 + 0.05 * x - 1.5
    elif compound == MEDIUM:
        return 0.0008333 * x ** 2 + 0.01 * x - 0.4
    else:
        return 0.00007 * x ** 2 + 0.01 * x + 0

def laptime_model(lap_numbers, lap_times, compound):

    def tyre_degradation_model_beta(x, beta):
        return tyre_degradation_model(x, compound) + beta
        # if compound == SOFT:
        #     return 0.0025 * x ** 2 + 0.05 * x - 1.5 + beta
        # elif compound == MEDIUM:
        #     return 0.0008333 * x ** 2 + 0.01 * x - 0.4 + beta
        # else:
        #     return 0.00007 * x ** 2 + 0.01 * x + 0 + beta



    popt, pcov = curve_fit(tyre_degradation_model_beta, lap_numbers, lap_times)
    return (popt, pcov, tyre_degradation_model)
