# -*- coding: utf-8 -*-
"""
point_in_polygon.py

How to conduct Point in Polygon queries in geopandas

Created on Tue Nov 13 13:50:13 2018

@author: cscuser
"""


import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.speedups

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
shapely.speedups.enable()

# Filepath to KML file
fp = "L4_data/PKS_suuralue.kml"
fpa = "L4_data/addresses.shp"


# Read file
polys = gpd.read_file(fp, driver='KML')
polys.plot()
data = gpd.read_file(fpa)

# Select the area of interest
southern = polys.loc[polys['Name'] == 'Eteläinen']

# Reset index and drop the original index column
southern = southern.reset_index(drop=True)

# Conduct Point in Polygon query
pip_mask = data.within(southern.loc[0,'geometry'])

# Select the points that 
pip_data = data.loc[pip_mask]

# Visualize the selection
ax = polys.plot(facecolor='gray')
ax = southern.plot(facecolor='red')
ax = pip_data.plot(ax=ax, color='gold', markersize=3)
