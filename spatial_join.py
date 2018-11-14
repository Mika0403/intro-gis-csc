# -*- coding: utf-8 -*-
"""
spatial_join.py

How to conduct spatial join using geopandas

Created on Tue Nov 13 14:46:44 2018

@author: cscuser
"""


import geopandas as gpd


import geopandas as gpd

# Filepath
pop_fp = "L4_data/Vaestotietoruudukko_2015.shp"
point_fp = "L4_data/addresses.shp"

# Read the data
pop = gpd.read_file(pop_fp)
points = gpd.read_file(point_fp)

# pop.plot(column="ASUKKAITA')
# Ensure that the datasets are the same projection
points = points.to_crs(crs=pop.crs)

# check that the CRS matches
pop.crs == points.crs
assert pop.crs == points.crs, "The CRS of the layers do not match"

# Make spatial join
join = gpd.sjoin(points, pop, how="inner", op='within')

join.plot(column='ASUKKAITA', cmap='Reds', markersize=join['ASUKKAITA']/1642 + 100, legend=True)

