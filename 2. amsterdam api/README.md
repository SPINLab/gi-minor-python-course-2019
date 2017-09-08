# Chapter 2. Amsterdam API



## Assignment

Task 1. Download a single panorama photo through the API
 
Task 2. Download a photo based on a location through the API, save its location in a shapefile, and create a usable hyperlink to the photo in ArcMap

Task 3. Download the first 5 pages of photos. Save the locations in a shapefile, import into ArcMap and create hyperlinks to open them.

Task 4. (optional) Download a series of photos in a single street.

## Introduction to Requests

To retrieve data from the API we will use the `requests` module. Requests is a fairly straight forward, easy to use, and powerful library for sending requests over the internet (HTTP).

Requests retrieves data from an url, which can be a website, an image, or any other file. It stores the response from the server in an python object. From this object you can get all the needed infarmation.

A basic request using requests looks like this:

First we import the module:
```python
import requests
```

Then we request data using a url (in this case a website):
```python
r = requests.get('https://github.com/clucas111/gi-minor-python-course')
```

The website (html file) is now stored in the response object `r`. You can see the content as follows:
```python
print r.content
```
Or if you are using python 3:
```python
print(r.content)
```

## Getting Started

1. Go to the [Amsterdam API website](https://api.data.amsterdam.nl/api/), look for the panorama photos API and click on the `Online API` link. Explore the API (what directories are there? What data do they return? Which options do they have?)

2. Open `photo_single.py`. Create a python script which retrieves a single photo from the API and saves it to the hard disk. The `.py` file contains pointers and hints to help you.

## Using parameters

1. Open `photo_location.py`. Create a python script which retrieves a photo based on a location (for example in front of your house or the university) and save the photo and a shapefile with the location to the hard disk. The `.py` file contains pointers and hints to help you.

2. Load the shapefile into ArcMap and make the point clickable, linking to the photo, by creating a hyperlink based on a field (path to the photo on the hard disk) in the shapefile. HINT: The ability to create a hyperlink based on a field is given in the `Display` tab of the `Layer Properties`. To be able to click on the point enable hyperlink mode by clicking on the lightning bolt icon on the toolbar:

    ![alt text](hyperlink.png "Hyperlink Mode")

## Retrieving larger amounts of data

1. Open `photo_pages.py`. Create a python script which retrieves the first 5 pages of photos made in 2016. Also think about how you could make a script that downloads all photos of 2016 (don't run it because its a large amount of data and will take a long time). Again save the photos and a shapefile with the locations to the hard disk.

2. Load the shapefile into ArcMap and make the photo locations clickable.

## Retrieving a series of photos (optional)

Since the API only allows to get the single closest photo to a location it is a bit of a challenge to download a series of photos in a street.

1. Think of a way to achieve this task. It can be done in multiple ways.

2. Make a python script. And visualize in ArcMap the same way as before.
