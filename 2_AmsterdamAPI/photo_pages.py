import requests
import fiona
from fiona.crs import from_epsg


# Request the first page of the 2016 directory of the API. And create a dictionary from it.
response = requests.get('https://api.data.amsterdam.nl/panorama/recente_opnames/2016/')
response_dict = response.json()

# open (create) a shapefile. Look at the previous exercise how to define the
# schema and crs, and create a shapefile with fiona using the schema and crs.

crs = from_epsg(4326)
schema = {'geometry': 'Point',
          'properties': {'Path': 'str',
                         'Name': 'str',
                         'DateTime': 'datetime'}}

shp_filepath = 'photo_locations.shp'

with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:
    ## Run for, for example, 5 pages
    # HINT: use a for loop. Look at the recap how to create a for loop.
    # HINT: use the range(*) function to create a list to loop through. * is the number.
    for page in range(5):
        ## run through each result of the page
        # HINT: use a for loop. Again look at the recap to see how to loop through a list
        for result in response_dict['results']:
            ## Save the image of the result to the hard disk. Like we did in previous exercises.
            url = result['image_sets']['equirectangular']['full']
            image = requests.get(url)

            filename = result['filename']
            with open(filename, 'wb') as f:
                f.write(image.content)

            ## write the location and properties to the shapefile. Like we did in previous exercises.
            shp.write({'geometry': result['geometrie'],
                       'properties': {'Path': "C:\\Projects\\SPINLab\\GI-minor\\gi-minor-python-course\\2_AmsterdamAPI\\" + filename,
                                      'Name': result['filename'],
                                      'DateTime': result['timestamp']}})

        ## Get the url of the next page
        # HINT: look through the response dictionary for a link to the next page
        next_url = response_dict['_links']['next']['href']
        ## Request the next page using the requests module. And create a dictionary from it.
        response = requests.get(next_url)
        response_dict = response.json()
