import requests
# documentation: http://docs.python-requests.org/en/master/

## request data
    # request data from the amsterdam panorama API
    # (url: https://api.data.amsterdam.nl/panorama/recente_opnames/2016/)
    # HINT: use the `get` function of the `requests` module
response = requests.get('https://api.data.amsterdam.nl/panorama/recente_opnames/2016/')
## create a python dictionary from the response
    # HINT: use the json method of the response object
    # You can display the methods available of an object by typing:
    # dir(*object_name*) for a simple list of functions and attributes or
    # help(*object_name*) for a list of functions and attributes with
    # a description (if written by the author of the class)
response_dict = response.json()

## retrieve the image url
    # retrieve the url from the response dictionary
    # HINT: explore the dictionary using the variable explorer
    # available in spyder.
    # HINT: how do we get a value out of a dictionary?
url = response_dict['results'][0]['image_sets']['equirectangular']['full']
## request the image
    # use the image url to get the image
    # HINT: remember how we used the `requests` module to retrieve data from an url?
image = requests.get(url)

## save the image to the hard disk
    # save the image to the data/ directory
    # use the filename as defined in the response dictionary
    # HINT: remember how we wrote data to a file?
    # HINT: to write bytes to a file instead of text, use 'wb' instead of just 'w'
    # when opening the file.
    # HINT: use dir() or help() to list the methods and attributes of the
    # image response. which method of attribute could give the image in a
    # format we can write to a file?
filename = 'data\\' + response_dict['results'][0]['filename']
with open(filename, 'wb') as f:
    f.write(image.content)
