# Chapter 2. Spatial data

In this chapter you'll learn how to read spatial data stored in a Shapefile, perform some basic calculcations and analysis, and store the results in a new Shapefile. 

## Assignment

You are asked to calculate the area, perimeter and geometry of the intersection between any geometry pair in `data/data.shp`. `data.shp` contains the geometries shown below.

   
![](https://github.com/ndkv/gi-minor-python-course/raw/master/2.%20geodata/data/data.png)

Use the provided `intersect.py` script as a starting point (see below).

You'll successfully pass this assignment when your script's output matches that of the tutor.

## Suggested approach

1. open `intersect.py`
2. follow the instructions (comments) and implement the asked functionality:
    1. read `data/data.shp`
    2. intersect one of the features with the other features
    3. calculate the area and perimeter of the intersection
    4. store the geometry of the intersection in a new Shapefile
3. run your code and compare your answers to the tutor's answers 

Please refer to the documentation of each module to figure out which functions to use (see below).

## Modules and documentation

By itself Python is not capable of dealing with Shapefiles and perfoming geospatial analyses. Fortunately, Python's capabilities can be extended through modules. In this exercise we'll use the following modules:

|module|purpose|documentation|
|---|---|---|
|pyshp|read/write Shapefiles|https://github.com/GeospatialPython/pyshp|
|Shapely|perform spatial analysis|http://toblerity.org/shapely/manual.html|

`pyshp` contains fuctionalities to read Shapefiles, extract features and their geometries and attributes.

`Shapely` is capable of creating spatial objects such as `Points`, `Lines` and `Polygons` and calculating their areas, perimeters, etc. 
  
See `intersect.py` for hints and usage examples.

## Getting help

- Please use the [issue tracker](https://github.com/ndkv/gi-minor-python-course/issues). [It's good for us, it's good for you.](https://github.com/ndkv/gi-minor-python-course#getting-help).
- Ask an assistant for help.