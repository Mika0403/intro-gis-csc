# -*- coding: utf-8 -*-
"""

geocode_addresses.py

How to convert addresses to Points and vica versa

Created on Tue Nov 13 10:19:50 2018

@author: cscuser
"""

import geopandas as gdb
import pandas as pd

# Import the geocoding tool and geopy
from geopandas.tools import geocode

import contextily as cxt

def add_basemap(ax,zoom,url):
    xmin,xmax,ymin,ymax = ax.axis()

# Filepath 
fp="L3_data/addresses.txt"

# read the data
data=pd.read_csv(fp,sep=';')

# Geocode the addresses from 'addr'
# nominatim on palvelu
geo = geocode(data['addr'], provider='nominatim', user_agent='csc_user_ht')

# Merge geoceded locations back to the original DataFrame
geo=geo.join(data)

# Reproject to the Web Mercator
#
geo = geo.to_crs(epsg=3857)
# plot the data
geo.plot()

add_basemap(ax=ax,zoom=13)
