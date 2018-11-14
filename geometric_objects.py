# -*- coding: utf-8 -*-
"""
geometric_objects.py

Intro...

Requirements...
    -
Created on Mon Nov 12 10:59:04 2018

@author: cscuser
"""

# alku


# Import necessary geometric objects from shapely module
from shapely.geometry import Point, LineString, Polygon


# Create Point geometric object(s) with coordinates
point1 =  Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)

print (point3D)
type(point1)

#Pointstring
#-------

# koordinaatit 
point_coord = point1.coords

# xy -koordinaatit
xy = point1.xy
print (xy)

# get x and y
x = point1.x
y = point1.y
 
# calc distance
point_dist = point1.distance(point2)

print (point_dist)

# create buffer 20
point_buff = point1.buffer(20)

#Linestring
#-------

# create line based on ...
line = LineString([point1, point2, point3])

# create line based on coordinate tuples...
line2 = LineString([(2.2,4.2),(7.2,-25-1) ,(9.26,-2.456) ])

#coordinates
lxy = line.xy

# get x and y coord
x = line.xy[0]
y = line.xy[1]

# get the length
l_length = line.length

# get the center
l_centroid = line.centroid

# polygon
#--------
for x in range(5):
    print (x)
    
# create polygon based on tuples
poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

# create polygon based on Point
poly2 = Polygon([(point1.xy), (point2.xy), (point3.xy)])
#
point_list = [point1,point2,point3]
poly3 = Polygon([(p.x,p.y) for p in point_list])

[(p.x,p.y) for p in point_list]

# Get geometry type as string
type_poly = poly.geom_type

# calculate area
poly_area = poly.area

# centroid
poly_cent = poly.centroid

# bounding box
poly_bound = poly.bounds

# create bounding box geometry
from shapely.geometry import box

# unpack the bounding box coordinates with asterix(*)
poly_bbox = box(*poly_bound)

# get exterior
poly_exterior= poly.exterior

# lenght of ex
poly_ext_len = poly.exterior.length

# polygon with hole
#----------------
# Exterior of the world in desimal degrees
world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
# create a large hole leaving 10 desimal boundary
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]

# World without a hole
world = Polygon(shell=world_exterior, holes=hole)























