# Chapter 2. Spatial data

In this chapter you'll learn how to read spatial data stored in a Shapefile, perform some basic calculcations and analysis, and store the results in a new Shapefile. 

## Assignment

You are asked to calculate the area, perimeter and geometry of the intersection between any geometry pair in `data/data.shp`. `data.shp` contains the geometries shown below.

   
![](https://github.com/ndkv/gi-minor-python-course/raw/master/2.%20geodata/data/data.png)

## Steps

1. open `intersect.py`
2. follow the instructions (comments) and implement the asked functionality:
    1. read `data/data.shp`
    2. intersect one of the features with the other features
    3. calculate the area and perimeter of the intersection
    4. store the geometry of the intersection in a new Shapefile
3. run your code and compare your answers to the tutor's answers 

Pleaes refer to the documentation of each module to figure out which functions to use (see below).

## Modules and documentation

By itself Python is not capable of dealing with Shapefiles and perfoming geospatial analyses. Fortunately, Python's capabilities can be extended through modules. In this exercise we'll use the following modules:

|module|purpose|documentation|
|---|---|---|
|pyshp|read/write Shapefiles|https://github.com/GeospatialPython/pyshp|
|Shapely|perform spatial analysis|http://toblerity.org/shapely/manual.html|

See `intersect.py` for an example how to invoke modules in a script.

## Getting help

- Use the [issue tracker](https://github.com/ndkv/gi-minor-python-course/issues). See how and why [here](https://github.com/ndkv/gi-minor-python-course#getting-help).
- Ask an assistant for help.