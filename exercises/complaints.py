# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:02:30 2015

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

complaints = pd.read_csv(data_folder + '311-service-requests.csv')

#==============================================================================
# Plot types of complaints histogram
#==============================================================================

complaint_counts = complaints['Complaint Type'].value_counts()

# Plot the first 10
plt.figure()
complaint_counts[:10].plot(kind='bar')


#==============================================================================
# Noise Complaints
#==============================================================================
# Select only noise complaints
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]

# Select noise complaints from brooklyn
in_brooklyn = complaints['Borough'] == "BROOKLYN"
noise_in_brooklyn = complaints[is_noise & in_brooklyn][['Complaint Type', 
                                    'Borough', 'Created Date', 'Descriptor']]

# Get counts per borough
noise_complaint_counts = noise_complaints['Borough'].value_counts()
plt.figure()
noise_complaint_counts.plot(kind='bar')

# Look at noise complaints as a fraction of all complaints
complaint_counts = complaints['Borough'].value_counts()
plt.figure()
(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')




















