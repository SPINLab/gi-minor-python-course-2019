import requests
import fiona
from fiona.crs import from_epsg


cwd = "C:\\Projects\\SPINLab\\GI-minor\\gi-minor-python-course\\2. amsterdam api"

target_dir = 'data\\pages\\'
num_pages = 5

## request the first page
response = requests.get('https://api.data.amsterdam.nl/panorama/recente_opnames/2016/')
response_dict = response.json()

## open a shapefile
crs = from_epsg(4326)
schema = {'geometry': 'Point',
          'properties': {'Path': 'str',
                         'Name': 'str',
                         'DateTime': 'datetime'}}

shp_filepath = target_dir + 'photo_locations.shp'
with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:
    ## To extract all photos (WARNING: takes a LONG time and is a LOT of data):
    # next_url = ''
    # while next_url is not None:
    ## Run for 5 pages
    # HINT: use a for loop
    for page in range(num_pages):
        ## run through each result of the page
        # HINT: use a for loop
        for result in response_dict['results']:
            ## Save the image of the result to the hard disk
            url = result['image_sets']['equirectangular']['full']
            image = requests.get(url)

            filename = target_dir + result['filename']
            with open(filename, 'wb') as f:
                f.write(image.content)
            ## write the location and properties to the shapefile
            shp.write({'geometry': result['geometrie'],
                       'properties': {'Path': cwd + '\\' + filename,
                                      'Name': result['filename'],
                                      'DateTime': result['timestamp']}})
        ## Get the url of the next page
        # HINT: look through the response dictionary for a link to the next page
        next_url = response_dict['_links']['next']['href']
        ## Request the next page
        response = requests.get(next_url)
        response_dict = r.json()
