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



def laptime_model(lap_numbers, lap_times, trackwear):

    def tyre_degradation_model(x, beta):
        a = 0.03 * trackwear / 60
        b = 0.01 * trackwear
        c = 0

        return a * x ** 2 + b * x + c + beta


    popt, pcov = curve_fit(tyre_degradation_model, lap_numbers, lap_times)
    return (popt, pcov, tyre_degradation_model)
