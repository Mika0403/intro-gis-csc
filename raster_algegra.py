# -*- coding: utf-8 -*-
"""
raster_algegra.py

How to do raster calculations useing rasterio and numpy

Created on Wed Nov 14 12:58:12 2018

@author: cscuser
"""

import rasterio
import numpy as np
from rasterio.plot import show
import os
import matplotlib.pyplot as plt

#Data directory
data_dir = "L5_data"

# Filepath
fp = os.path.join(data_dir, "Helsinki_masked.tif")

# Open the data
raster = rasterio.open(fp)

# Read channals for red and NIR
red = raster.read(3)
nir = raster.read(4)

# Statistics
red.mean()
nir.mean())

show(nir, cmap='terrain')

# Convert to floats
red = red.astype('f4')
# red.dtype
nir = nir.astype('f4')

# Ignore 'division by zero' exception
np.seterr(divide='ignore', invalid='ignore')

# Calculate NDVI using numpy arrays
ndvi = (nir - red) / (nir + red)

# Plot the ndvi with legend
plt.imshow(ndvi,cmap='terrain_r')
plt.colorbar()

# RdYlBu
plt.imshow(ndvi,cmap='RdYlBu')

# Time series
# change = year2018 - year2008
