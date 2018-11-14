# -*- coding: utf-8 -*-
"""
read_cloud_optimized_geotiffs.py
https://automating-gis-processes.github.io/CSC/notebooks/L5/read-cogs.html

Created on Wed Nov 14 15:07:49 2018

@author: cscuser
"""

import rasterio

import matplotlib.pyplot as plt
import numpy as np

# Specify the path for Landsat TIF on AWS
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

src = rasterio.open(url)

#with rasterio.open(url) as src:
#    print(src.profile)

# Get the list of overviews
oviews = src.overviews(1)
oview = oviews[-1]
oview_2 = oviews[2] # indeksi

# Read a thumbnail using low relolution source
#
thumbnail = src.read(1, out_shape=(1, 
                                   int(src.height // oview), 
                                   int(src.width // oview)))

thumbnail_2 = src.read(1, out_shape=(1, 
                                   int(src.height // oview_2), 
                                   int(src.width // oview_2)))

# plot
show(thumbnail, cmap = 'terrain')
show(thumbnail_2, cmap = 'terrain')

# retrieve a "Window" (a subset) from full resolution raster
window = rasterio.windows.Window(1024, 1024, 1280, 2560)

# retrieve a subset of the data
subset = src.read(1,window=window)

# plot the subset
show(subset, cmap= 'terrain')
