# -*- coding: utf-8 -*-
"""
nearest_point.py

How to get the nearest point of another

Created on Tue Nov 13 15:11:27 2018

@author: cscuser
"""

from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
import geopandas as gpd

def nearest(row, geom_union, df1, df2, 
            geom1_col='geometry', geom2_col='geometry', src_column=None):
    """
    
    Find the nearest point and return the corresponding value from specified column.
    
    Parameters
    ----------
    geom_union: shapely.Multipoint
    
    """

    # Find the geometry that is closest
    nearest = df2['geometry'] == nearest_points(row['geometry'], geom_union)[1]
    # or
    # nearest = df2[geom2_col] == nearest_points(row[geom1_col], geom_union)[1]

    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]

    return value


# Filepaths
    
try:
    
    fp1 = "L4_data/PKS_suuralue.kml"
    fp2 = "L4_data/addresses.shp"
    
    # Activate KML driver
    gpd.io.file.fiona.drvsupport.supported_drivers['KLM'] = 'rw'
    
    # Read data
    polys = gpd.read_file(fp1, driver='KML')
    src_points = gpd.read_file(fp2)
    
    # Unary union
    unary_union = src_points.unary_union
    
    # Calculate the centroid for the polygons
    polys['centroid'] = polys.centroid
    
    # Find the nearest PT station for the Polygon centroid
    #polys['nearest_id'] = polys.apply(nearest, geom_union=unary_union, 
    #     df1=polys, df2=src_points, geom1_col='centroid', src_column='id')
    
    polys['nearest_id'] = df1.apply(nearest, geom_union=unary_union, 
         df1=polys, df2=src_points, geom1_col='centroid', src_column='id', axis=1)

    print ('OK')
    
catch:
    print ('Error')
    
    