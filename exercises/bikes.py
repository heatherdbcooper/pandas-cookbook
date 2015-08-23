# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:46:41 2015

@author: Heather
"""
#==============================================================================
# Preamble
#==============================================================================

import pandas as pd
#from pandas import DataFrame
import matplotlib.pyplot as plt
#import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.family'] = 'sans-serif'

#==============================================================================
# Read in Data
#==============================================================================

data_folder = 'C:\\Users\\Heather\\Documents\\GitHub\\pandas-cookbook\\data\\'

# This one is broken - encoding wrong and separator wrong
broken_df = pd.read_csv(data_folder + 'bikes.csv')

# This one works as we have now fixed the inputs
fixed_df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', 
                       parse_dates=['Date'], dayfirst=True, index_col='Date')
plt.figure()                     
fixed_df.plot()

# So now put it into a neatly named df
bikes = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
plt.figure()
bikes['Berri 1'].plot()

#==============================================================================
# Looking at the berri bike path
#==============================================================================

berri_bikes = bikes[['Berri 1']].copy()

# Add the weekday column
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure()
weekday_counts.plot(kind='bar')





