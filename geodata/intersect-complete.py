# documentation: https://github.com/GeospatialPython/pyshp
import shapefile

# documentation: http://toblerity.org/shapely/manual.html
from shapely.geometry import Polygon

##
## Load data
##

# read data.shp from the data/ directory
# HINT: use shapefile's Reader "function"

sf = shapefile.Reader('data/data.shp')

##
## Create Python data structures
##

# put all features from data/data.shp in a Python list

shapes = sf.shapes()

# extract the main feature you'll be checking for intersections
# HINT: which list function removes an item from a list while returning it to you?

main_shape = shapes.pop()

##
## Calculate areas and perimeter
##

# calculate the main feature's area and perimeter using Shapely
# HINT: create a Shapely Polygon and use its area and length properties

main_feature = Polygon(main_shape.points)
area = main_feature.area
perimeter = main_feature.length

# print the feature's id
# HINT: look it up in the attribute table with the shapefile.Reader.records() function

records = sf.records()
main_records = records.pop()

print main_records[0]

##
## Check for intersections
##

# Use Shapely's intersection function to check whether your main feature
# intersects any of the other features.
# HINT: use the Shapely is_empty function to check whether an 
# intersection between two geometries exists 
# HINT: you'll need to convert each feature into a Shapely Polygon to be 
# able to perform the intersection check

# Store each intersection in a list
intersections = []

for shape in shapes:
	feature = Polygon(shape.points)

	intersection = main_feature.intersection(feature)

	if intersection.is_empty:
		print "These geometries do not intersect!"
	else:
		print "Found an intersection!"
		intersections.append(intersection)

##
## Save the intersections to a file
##

# add the intersections to data.shp and store them in a new file called polygons.shp
e = shapefile.Editor(shapefile="data/data.shp")

for intersection in intersections:
	# create a new shapefile polygon using the shapefile.Editor.poly function
	# HINT: you'll need to convert the intersection's Shapely geometry into 
	# a format that fits into the shapefile.Editor.poly function

	e.poly(parts=[intersection.exterior.coords])

	# Populate the attribute table 
	e.record("", "intersect", intersection.area)

# write the changes to data/data.shp to a new file
e.save("data/polygons.shp")