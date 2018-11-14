# -*- coding: utf-8 -*-
"""
visualize_raster.py

Visualizing raster data with Rasterio

Created on Wed Nov 14 10:04:17 2018

@author: cscuser
"""


import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import numpy as np
import os
import matplotlib.pyplot as plt
from rasterio.plot import show_hist

# import Normilize() fuction from raster_tools Python script
from raster_tools import normalize

# Filepath
data_dir = "L5_data"
fp = os.path.join(data_dir, 'Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif')

# basename
filename = os.path.basename(fp)

# Open the file
raster = rasterio.open(fp)

# Plot the channel 1
show((raster,1))

show((raster,2))

# Plot channal 3 in alternative manner
show(raster.read(3))

# Visualize channel 1,2, 
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=1,ncols=3,figsize=(10,4),sharey=True)
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, nrows=1, figsize=(10, 4), sharey=True)

# Plot
show((raster,3), cmap='Reds',ax=ax1)
# show((raster,2), cmap='Green',ax=ax2)
show((raster, 2), cmap='Greens', ax=ax2)
# show((raster,1), cmap='Blue',ax=ax3)
show((raster, 1), cmap='Blues', ax=ax3)

# Set titles
ax1.set_title("Red")
ax2.set_title("Green")
ax3.set_title("Blue")

# Create a True Color composite
# -----------------------------

# Read channels into arrays
red = raster.read(3)
green = raster.read(2)
blue = raster.read(1)

# Normalize the bands
redn = normalize(red)
greenn = normalize(green)
bluen = normalize(blue)

# Create the composite
rgb = np.dstack((redn,greenn,bluen))

# Ploit the RGB figure
plt.imshow(rgb)

# Histogram of the raster dat
show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3,
      histtype='stepfilled', title="Histogram")









