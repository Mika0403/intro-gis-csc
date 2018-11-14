# -*- coding: utf-8 -*-
"""

map_projections.py

Map projections
    
Created on Mon Nov 12 15:25:01 2018

@author: cscuser
"""

# 
import geopandas as gpd
import matplotlib.pyplot as plt

# filepath
fp = "L2_data/Europe_borders.shp"

data = gpd.read_file(fp)

# 
print(data.crs)

# reproject the GeoDataFrame to EPSG 3035
geo = data.copy()
geo = geo.to_crs(epsg=3035)

# plot and see the diff
# ----------------------

# create subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))

# plot WGS84 to ax1
data.plot(ax=ax1, facecolor='gray')
geo.plot(ax=ax2, facecolor='blue')

# set titles
ax1.set_title("WGS84", fontsize=16)
ax2.set_title("lambert", fontsize=16, color='red')

# save the fig on disk
plt.savefig("projections.png", dpi=300)

# save reprojected data to disk
outfp = "L2_data/Europe_borders_proj3035.shp"

geo.to_file(outfp)

# Fix the CRS
import pycrs

proj4 = pycrs.parser.from_epsg_code(3035).to_proj4()

geo.crs = proj4

geo.crs = pycrs.parser.from_epsg_code(3035).to_proj4()

epsg_code = 3035
geo.crs = pycrs.parser.from_epsg_code(epsg_code).to_proj4()
