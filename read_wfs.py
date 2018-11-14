# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:29:40 2018

read_wfs.py

@author: cscuser
"""

import geopandas as gdb
import requests 
import geojson

# url
url="http://geo.stat.fi/geoserver/vaestoruudut/wfs"

# Get capabalities
capabilities_param  = dict(service='WFS', request='GetCapabilities')

# request
capabilities=requests.get(url,params=capabilities_param)
print(capabilities.content)

# specify the parameters for fetching the data
params = dict(service='WFS', version='2.0.0', request='GetFeature',
          typeName='vaestoruutu:vaki2017_5km',outputFormat='json')

# Fetch the data from WFFS
r=requests.get(url,params=params)

# Create a GeoDataFrame from the response
data=gdb.GeoDataFrame.from_features(geojson.loads(r.content))

# Define CRS
data.crs={'init':'epsg:3067'}

# Specify parameters (read data in json format)
params = dict(service='WFS', version='2.0.0', request='GetFeature',
         typeName='vaestoruutu:vaki2017_5km', outputFormat='json')

# Fetch data from WFS using requests
r = requests.get(url, params=params)

# Create GeoDataFrame from geojson
data = gdb.GeoDataFrame.from_features(geojson.loads(r.content))
