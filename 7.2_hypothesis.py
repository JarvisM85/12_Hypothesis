# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:22:41 2024

@author: sahil
"""

import pandas as pd

import numpy as np

import scipy
from scipy import stats
import statsmodels.stats.descriptivestats as sd
import statsmodels.stats.weightstats
import statsmodels.stats.stests

####    1 =>   Z-test

fabric = pd.read_csv("C:/DS2/7_Hypothesis/hypothesis_datasets/Fabric_data.csv")
fabric


print(stats.shapiro(fabric))
np.mean(fabric)

# Z-test
ztest, pval = stests.ztest(fabric, x2= None, value=150)
print(float(pval))

############################################################

####   Mann-Whitney test ##################
# - ------------------------  #

fuel = pd.read_csv("C:/DS2/7_Hypothesis/hypothesis_datasets/mann_whitney_additive.csv")
fuel

fuel.columns = "Without_additive","With_additive"


# normally test
# H0: data is normal

print(stats.shapiro(fuel.Without_additive))
print(stats.shapiro(fuel.With_additive))

scipy.stats.mannwhitneyu(fuel.Without_additive,fuel.With_additive)



##################################################
####    Paired  T-Test   ###############
#     -----------------        #

sup = pd.read_csv("C:/DS2/7_Hypothesis/hypothesis_datasets/paired2.csv")
sup.describe()

stats.shapiro(sup.SupplierA)
stats.shapiro(sup.SupplierB)

import seaborn as sns
sns.boxplot(data=sup)

ttest, pval = stats.ttest_rel(sup['SupplierA'], sup['SupplierB'])
print(pval)



##################################################
####    2- Sample  T-Test   ###############
#     -----------------        #

prom = pd.read_excel("C:/DS2/7_Hypothesis/hypothesis_datasets/Promotion.xlsx")
prom

# Ho: InterestRateWaiver  < StandardPromotion
# Ha: InterestRateWaiver  > StandardPromotion

prom.columns = "InterestRateWaiver","StandardPromotion"

#Normality test

stats.shapiro(prom.InterestRateWaiver)  #Shapiro Test

print(stats.shapiro(prom.StandardPromotion))

# Data are Noramal

# Variance test
help(scipy.stats.levene)
#H0= Both columns have equal variance
#H1= Both columns have equal variance
scipy.stats.levene(prom.InterestRateWaiver,prom.StandardPromotion)

# 2. Sample T-test
scipy.stats.ttest_ind(prom.InterestRateWaiver,prom.StandardPromotion)
help(scipy.stats.ttest_ind)
# Ho: equal means 
# Ha: unequal means




##################################################
#### ####     One Way ANOVA   ###############
#           -----------------        #

con_renewal = pd.read_excel("C:/DS2/7_Hypothesis/hypothesis_datasets/ContractRenewal_Data.xlsx")
con_renewal
con_renewal.columns = "SupplierA","SupplierB","SupplierC"


stats.shapiro(con_renewal.SupplierA)

stats.shapiro(con_renewal.SupplierB)

stats.shapiro(con_renewal.SupplierC)

help(scipy.stats.levene)

scipy.stats.levene(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC)


F, p = stats.f_oneway(con_renewal.SupplierA,con_renewal.SupplierB,con_renewal.SupplierC)





##################################################
####                      ###############
#     -----------------        #

two_prop_test = pd.read_excel("C:/DS2/7_Hypothesis/hypothesis_datasets/JohnyTalkers.xlsx")
two_prop_test

from statsmodels.stats.proportion import proportions_ztest

tab1 = two_prop_test.Person.value_counts()
tab1

tab2 = two_prop_test.Drinks.value_counts()
tab2

# cross-table
pd.crosstab(two_prop_test.Person, two_prop_test.Drinks)

count = np.array([58,152])
nobs = np.array([480,740])

stats, pval = proportions_ztest(count, nobs,alternative = 'two-sided')
print(pval)

stats, pval = proportions_ztest(count, nobs,alternative = 'larger')
print(pval)





##################################################
#### ####     CHI Square Test   ###############
#           -----------------        #

Bahaman = pd.read_excel("C:/DS2/7_Hypothesis/hypothesis_datasets/Bahaman.xlsx")
Bahaman

count = pd.crosstab(Bahaman["Defective"], Bahaman["Country"])
count
Chisquares_results = scipy.stats.chi2_contingency(count)

Chi_square = [['Test Statistic','p-value'],[Chisquares_results[0],Chisquares_results[1]]]
Chi_square

'''
you use chi2_contingency when you want to test
whether two (or more) groups have the same distribution.
'''

