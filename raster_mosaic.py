# -*- coding: utf-8 -*-
"""

raster_mosaic.py

How to create a raster mosaic using rasterio

Created on Wed Nov 14 13:21:06 2018

@author: cscuser
"""
import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import os
import matplotlib.pyplot as plt
import pycrs

# File and folder paths
data_dir = "L5_data"

# output filepath for the mosaic
output_fp = os.path.join(data_dir,"Helsinki_DEM_2x22m_mosaic.tif")

# Input files
search_criteria = "L*.tif"
q= os.path.join(data_dir,search_criteria)

# List files that matches the critetia
dem_fps = glob.glob(q)

# Open the source files with rasterio
src_files_to_mosaic = [rasterio.open(fp) for fp in dem_fps]
# rasterein maara
print(len(src_files_to_mosaic))

# Merge the rasters into mosaic
mosaic, out_trans = merge(datasets=src_files_to_mosaic)

# plot
show(mosaic,cmap='terrain')
plt.colorbar()

#plt.imshow(mosaic,cmap='terrain_r')
#plt.colorbar()

# Update meta data and save the mosaic
out_meta = src_files_to_mosaic[0].meta.copy()

# Update metadata with new dimension and crs
out_meta.update(
        {'height': mosaic.shape[1],
        'width': mosaic.shape[2],
        'transform': out_trans,
        'crs': "+proj=utm +zone=35 +ellps=GRS80 +units=m +no_defs "
        }
        )

# Write the mosaic to disk
with rasterio.open(output_fp,'w',**out_meta) as dest:
    dest.write(mosaic)

# plot
m = rasterio.open(output_fp)
plt.imshow(m.read(1),cmap='terrain')
# plt.colorbar()



    