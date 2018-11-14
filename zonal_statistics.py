# -*- coding: utf-8 -*-
"""
zonal_statistics.py

To calculate zonal statistics using rasterio and rasters

Created on Wed Nov 14 13:53:06 2018

@author: cscuser
"""

import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gdb
import os
import matplotlib.pyplot as plt


# Filepath
data_dir = "L5_data"
dem_fp = os.path.join(data_dir,"Helsinki_DEM_2x22m_mosaic.tif")

# Read the data
dem = rasterio.open(dem_fp)

# Fetch the Polygons for zonal statistics from OSM
kallio_q = "Kallio,Helsinki,Finland"
pihlajamaki_q = "Pihlajamäki,Malmi,Helsinki,Finland"

# retrieve the geometrics from OSM
kallio = ox.gdf_from_place(kallio_q)
pihjalamaki = ox.gdf_from_place(pihlajamaki_q)

# Test that crs matches
assert kallio.crs == dem.crs, "CRS do not match between layers."
assert pihjalamaki.crs == dem.crs, "CRS do not match between layers."

# Reproject the project 
# "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
kallio = kallio.to_crs(crs="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")
# pihjalamaki = pihjalamaki.to_crs(crs=dem.crs)
pihjalamaki = pihjalamaki.to_crs(crs="+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs ")

# Plot the areas on top of the raster
ax = kallio.plot(facecolor='None', edgecolor='red',linewidth=2)
ax = pihjalamaki.plot(ax=ax,facecolor='None', edgecolor='blue',linewidth=2)
                      
# Plot the raster below
show((dem,1), ax=ax)

#
array = dem.read(1)
affine = dem.transform

# calculate stats
zs_kallio = zonal_stats(kallio,array, 
                        affine=affine, 
                        stats=['min', 'max', 
                               'mean', 'median', 
                               'majority'])

zs_pihjalamaki = zonal_stats(pihjalamaki,array, 
                        affine=affine, 
                        stats=['min', 'max', 
                               'mean', 'median', 
                               'majority'])

if zs_kallio[0]['max'] > zs_pihjalamaki[0]['max']:
    print ("Kallio is higher")
else:
    print ("Pihjalamäki is higher")
    
# huom, voidaan loopata polygon aineiston kohteiden mukaan, 
# ks. https://pythonhosted.org/rasterstats/manual.html#basic-example

# Dictionary 
zs_results = {}

for channel in range(1,5):
    zs_results[channel] = zonal_stats(polygon,channels_data_array, stats=['min', 'max'])
    

