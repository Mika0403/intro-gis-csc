# -*- coding: utf-8 -*-
"""

read_raster.py

Created on Wed Nov 14 09:16:40 2018

@author: cscuser
"""

import rasterio
import os
import numpy as np

# Data dir
data_dir = r"C:\IntroCSC" # 
fp = os.path.join(data_dir,'L5_data','Helsinki_masked_p188r018_7t20020529_z34__LV-FIN.tif')

#fp1 = os.path.join(data_dir,'L5_data')

# Open the file:
raster = rasterio.open(fp)
#raster1 = rasterio.open(fp1)
print (raster.crs)

# Affine transform
raster.transform

# Dimensions of the raster
raster.width
raster.height

# Number of channels
raster.count

# Bounds of the file
raster.bounds

# Driver
raster.driver

# No Data value
raster.nodatavals

# ALL metadata at once
raster.meta

# Read the data values to Python
# ------------------------------
band1 = raster.read(1)

# Access the data type
data_type = str(band1.dtype)

# Calculate basic statistics 
# --------------------------
# Read all bands
array = raster.read()

# Skip rows
skip = 4

# Calculate statistics for each band
stats = []
for idx,band in enumerate(array):
    if idx < skip:
        continue
    
    band_stat = {
        'min': band.min(),
        'mean': band.mean(),
        'median': np.median(band),
        'max': band.max(),
        'std': band.std()
        }
    channal_stat = {'channal %s' % (idx+1): band_stat}
    # "Hello {name}!".format(name="Heikki Hopo")
    stats.append(channal_stat)












    