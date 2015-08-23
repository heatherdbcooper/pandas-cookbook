# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:50:24 2015

@author: Heather
"""


#==============================================================================
# Preamble
#==============================================================================
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.family'] = 'sans-serif'


#==============================================================================
# Read in Data
#==============================================================================

data_folder = 'C:\\Users\\Heather\\Documents\\GitHub\\pandas-cookbook\\data\\'

weather_2012_final = pd.read_csv(data_folder + 'weather_2012.csv', index_col='Date/Time')
plt.figure()
weather_2012_final['Temp (C)'].plot(figsize=(15, 6))

#==============================================================================
# Downloading data from a url
#==============================================================================

url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

url = url_template.format(month=3, year=2012)
weather_mar2012 = pd.read_csv(url, skiprows=14, 
                              index_col='Date/Time', 
                              parse_dates=True, encoding='latin1', header=True)

#==============================================================================
# Selecting and plotting the data
#==============================================================================

# Plot a column with weird symbols
plt.figure()
weather_mar2012[u"Temp (\xc2\xb0C)"].plot(figsize=(15, 5))

#Fix the column names to get rid of silly chars
weather_mar2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)', 
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag', 
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag', 
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill', 
    u'Wind Chill Flag', u'Weather']

# Get rid of columns with empty values
weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')

# Get rid of defunct columns
weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)

#==============================================================================
# Look at temperatures
#==============================================================================

temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()

#==============================================================================
# %% Getting a whole year of data
#==============================================================================

def download_weather_month(year, month):
    """ Downloads all the weather data for a year """
#    if month == 1:
#        year += 1
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=14, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


# Use list comprehension to create a list of dataframes containing each month's
# data
data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

weather_2012 = pd.concat(data_by_month)

weather_2012.to_csv(data_folder + 'weather_2012_downloaded.csv')








