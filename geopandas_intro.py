# -*- coding: utf-8 -*-
"""

geopandas_intro.py

Basic funstionalionalities of Geopandas library.

Created on Mon Nov 12 13:05:51 2018

@author: cscuser
"""

# alku

# 
import geopandas as gpd

import pandas as pd


# Filepath0
fp = "L2_data/DAMSELFISH_distributions.shp"

# red the file with Geopandas
data = gpd.read_file(fp)

# print the 1. row of the data
data.head(20)
data.tail(5)

# print columns
cols = data.columns


#plot the geometries
data.plot()

# write the first 50 rows of our data into a new Shapefile
outfp = "L2_data/DAMSELFISH_selectio.shp"

# Select the first rows
selection = data.head(50)

selection.to_file(outfp)

# 
import fiona
fiona.supported_drivers

# save as GeoJSON
outfp_geojson = "L2_data/DAMSELFISH_selection.geojson"
selection.to_file(outfp_geojson,driver="GeoJSON")

# Geometrien in GeoDataFrames
# ---------------------------
data.columns
data['geometry'].head()
sel_col = data[['geometry','BINOMIAL']]

# select by criteria
unique = data['BINOMIAL'].unique()
criteria = 'Stegastes acapulcoensis'

# 
fish_a = data.loc[data['BINOMIAL']==criteria]

import psycopg2

# tutustu geoalchemy2!!!
import geoalchemy2

# Initialize the connection 
# conn, cursor = psycopg2.connect()
# pgdata = gpd.read_postgis(sql="Select * from...;",con=conn)

# Iterate over GeoDataFrame
# hidas isoille aineistoille
#
# alternative 1;
for index, row in selection.iterrows():
    # calculate the area of each polygon
    poly_area = row['geometry'].area
    print (poly_area)

# alternative 2;
data['area'] = data.apply(lambda row: row['geometry'].area, axis=1)
 
def calculate_area(row):
    return row['geometry'].area

# alternative 3:
data['area2'] = data.apply(calculate_area, axis=1)

# Geometric attributs from GeoDataFrame
# -------------------------------------

# Calculate the area using geopandas directly
data['area3'] = data.area
data['centroid'] = data.centroid
    
# set the geometry source for GeoDataFrame
geo = data.copy()
geo = geo.set_geometry('centroid')
geo.plot()

# Drop the geometry colunm from gdf
geo = geo.drop('geometry',axis=1)

# Create a buffer from points
geo['burrer'] = geo.buffer(10)
geo = geo.set_geometry('buffer')

# save points
geo.to_file('geom_centroids.shp')

# Calculate basic stat
mean_area = geo['area'].mean()
mean_min = geo['area'].min()
mean_max = geo['area'].max()
mean_std = geo['area'].std()

# Calculate in (Geo)DataFrame
geo['areaX2'] = geo['area'] + geo['area2']



# Group the data by column 'BINOMIAL'
grouped = data.groupby('BINOMIAL')


# Iterate over the group object
for key, values in grouped:
    individual_fish = values

print(individual_fish)














































