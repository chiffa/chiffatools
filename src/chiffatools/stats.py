import numpy as np
from matplotlib import pyplot as plt
from itertools import combinations
from chiffatools.Linalg_routines import rm_nans
from chiffatools import hmm
from scipy.stats import ttest_ind
import scipy.cluster.hierarchy as sch
from scipy.ndimage.filters import gaussian_filter1d
from pprint import pprint
from chiffatools.dataviz import smooth_histogram
from basic_drawing import show_2d_array
from scipy.stats import norm, poisson, t

def Tukey_outliers(set_of_means, FDR=0.005, supporting_interval=0.5, verbose=False):
    """
    Performs Tukey quintile test for outliers from a normal distribution with defined false discovery rate
    :param set_of_means:
    :param FDR:
    :return:
    """
    # false discovery rate v.s. expected falses v.s. power
    q1_q3 = norm.interval(supporting_interval)
    # TODO: this is not necessary: we can perfectly well fit it with proper params to FDR
    FDR_q1_q3 = norm.interval(1 - FDR)
    multiplier = (FDR_q1_q3[1] - q1_q3[1]) / (q1_q3[1] - q1_q3[0])
    l_means = len(set_of_means)

    q1 = np.nanpercentile(set_of_means, 50*(1-supporting_interval))
    q3 = np.nanpercentile(set_of_means, 50*(1+supporting_interval))
    high_fence = q3 + multiplier*(q3 - q1)
    low_fence = q1 - multiplier*(q3 - q1)

    if verbose:
        print 'FDR:', FDR
        print 'q1_q3', q1_q3
        print 'FDRq1_q3', FDR_q1_q3
        print 'q1, q3', q1, q3
        print 'fences', high_fence, low_fence

    if verbose:
        print "FDR: %s %%, expected outliers: %s, outlier 5%% confidence interval: %s" % \
              (FDR*100, FDR*l_means, poisson.interval(0.95, FDR*l_means))

    ho = (set_of_means < low_fence).nonzero()[0]
    lo = (set_of_means > high_fence).nonzero()[0]

    return lo, ho
