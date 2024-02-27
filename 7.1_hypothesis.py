# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:36:54 2024

@author: sahil
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.stats.descriptivestats as sd
import statsmodels.stats.weightstats

#1 sample sign test for given dataset check whether scores 
#are not equal or less than 80
#H0 scores are either  equal or less than 80
#H1 scores are not equaln greater than 80
#Whenever there is single sample and data is not normal

marks = pd.read_csv("C:/DS2/7_Hypothesis/hypothesis_datasets/Signtest.csv")
#Normal QQ plot

import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#Data is not normal
#H0 Data is normal
#H1 Data is not normal

stats.shapiro(marks.Scores)
#p_value is 0.024>0.005, p is high null fly
#Decision data is not normal

############################################################

#Let us check the description of the data
marks.Scores.describe()
#1 ssample sign test
sd.sign_test(marks.Scores,mu0=marks.Scores.mean())

















