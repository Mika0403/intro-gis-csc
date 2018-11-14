# -*- coding: utf-8 -*-
"""
Classify data values based on common classifiers

Created on Tue Nov 13 13:08:33 2018

@author: cscuser
"""

import geopandas as gb

import pysal as ps

#Filepath
fp = "L3_data/TravelTimes_to_5975375_RailwayStation_Helsinki.geojson"

# Read the data
data = gb.read_file(fp)

# Exclude -1 value (NoData)
data = data.loc[data['pt_r_tt'] >=0]

# Plot using 9 classes and classify the values using "Fisher Jenks" classification
data.plot(column="pt_r_tt", scheme="Fisher_Jenks", 
          k=9, cmap="RdYlBu", linewidth=0, legend=True)

# Plot walking distance
data.plot(column="walk_d", scheme="Fisher_Jenks", k=9, cmap="RdYlBu", linewidth=0, legend=True)

# Natural_Breaks
# define classes
k = 12
# Initialize the natural breaks classifier
classifier = ps.Natural_Breaks.make(k)

#data.plot(column="pt_r_tt", scheme="Natural_Breaks", 
#          k=9, cmap="RdYlBu", linewidth=0, legend=True)

# classify the travel time value
classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt'
classifications = classifications.rename(columns={'pt_r_tt':'nb_pt_r_tt'})

# conduct table join based on index
data = data.join(classifications)

# create a map based on new classes
data.plot(column='nb_pt_r_tt',linewidth=0, legend=True)

# ax = data.plot(column='nb_pt_r_tt',linewidth=0, legend=True)

# create a custom classifier
class_bins = [10,20,30,40,50,60]

classifier = ps.User_Defined.make(class_bins)

custom_classifications = data[['pt_r_tt']].apply(classifier)

# Rename the column 'nb_pt_r_tt'
custom_classifications = custom_classifications.rename(columns={'pt_r_tt':'c_pt_r_tt'})

# conduct table join based on index
data = data.join(custom_classifications)

# create a map based on new classes
data.plot(column='nb_pt_r_tt',linewidth=0, legend=True)

# ax = data.plot(column='c_pt_r_tt',linewidth=0, legend=True)
















