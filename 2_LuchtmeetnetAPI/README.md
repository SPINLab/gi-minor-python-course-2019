# Chapter 2. Luchtmeetnet API

Data gets made available in different ways. Sometimes, for example, you simply go to a website and click a download link, sometimes you need to [scrape it off a website](https://realpython.com/python-web-scraping-practical-introduction/), and sometimes you can use an [API (application programming interface)](https://en.wikipedia.org/wiki/Application_programming_interface). An API is a set of definitions and methods for different computer software to communicate with each other. It is a general term, but in the context of data acquisition an API makes it easier to retrieve data in an automatic way. To make use of this automation we need a way to tell the computer how to use the API. This can be done using various tools and/or programming languages. We will use python to this end, since it is a very accessible and flexible programming language, with a lot of modules available able to provide a broad range of extra functionality. Python is also the programming language used by GIS packages such as ArcGIS (arcpy) and QGIS.

As a data source to practice with we are going to use an API of the Netherlands National Institute for Public Health and the Environment (or Rijksinstituut voor Volksgezondheid en Milieu (RIVM)), concerning the Luchtmeetnet (air measurements network). They publish the measurements of different chemical compounds in the air online, at https://api.luchtmeetnet.nl/open_api. The documentation of this API can be found at https://documenter.getpostman.com/view/1562017/RVnbBxf9. The techniques used in this exercise can also be used to download data from many more API's from other sources, since most API's follow a similar structure, which is called [REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

## Introduction to Requests

To retrieve data from the API we will use the `requests` module. Requests is a fairly straight forward, easy to use, and powerful library for sending requests over the internet (HTTP). Requests retrieves data from an url, which can be a website, an image, or any other file. It stores the response from the server in an python object. From this object you can get all the needed information. A basic request using requests looks like this:

First we import the module:

```python
import requests
```

Then we request data using a url (in this case a website):

```python
response = requests.get('https://github.com/SPINLab/gi-minor-python-course-2018/')
```

The website (html file) is now stored in the response object `response`. You can see the content as follows:

Python 2:

```python
print response.content
```

Python 3:

```python
print(response.content)
```

A REST API will always respond with [JSON](https://en.wikipedia.org/wiki/JSON) data. JSON is a file format that is very commonly used for sending data over the internet. It is composed of key-value pairs (using curly brackets {}) and lists (using square brackets []). An example (taken from Wikipedia):

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "isAlive": true,
    "age": 27,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        },
        {
            "type": "mobile",
            "number": "123 456-7890"
        }
    ],
    "children": [],
    "spouse": null
}
```

The observant reader will have noticed that this is exactly the format of Python dictionaries and lists. A response from Requests will have a [method specifically made to deal with JSON data](http://docs.python-requests.org/en/master/user/quickstart/#json-response-content) and will return a Python dictionary. Perfect for when we want to use the data in Python. It is used as follows:

```python
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
response_dictionary = response.json()
print(response_dictionary)
print(response_dictionary['userId'])
```

## Getting Started

1. Go to the [Luchtmeetnet API documentation](https://documenter.getpostman.com/view/1562017/RVnbBxf9). Explore the API (what directories are there? What data do they return? Which options do they have?)

2. Think of which url we can use to retrieve a list of measurement locations (stations) and how to retrieve information about a station.

3. Open `1_basic_info.py`. Create a python script which retrieves basic information from the API. The `.py` file contains pointers and hints to help you.

## Timeseries data

1. Which url could we use to request measurement data of a single station? Which parameters would we have to set?

2. Choose a location (for example the one in Amsterdam of the previous exercise) and retrieve the location number.

3. Open `2_timeseries.py`. Create a python script which retrieves measurement data of a station and plot the data. The `.py` file contains pointers and hints to help you.

## Geo data

1. Think of which data we need to request to make a map of all stations colored by the measurement of a chemical compound

2. Open 3_geo.py. Create a python script which retrieves the measurement data of a chemical compound for a single point in time for all of the Netherlands. The `.py` file contains pointers and hints to help you.
