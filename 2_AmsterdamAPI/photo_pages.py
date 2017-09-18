import requests
import fiona
from fiona.crs import from_epsg



## request the first page

## open a shapefile

    ## To extract all photos (WARNING: takes a LONG time and is a LOT of data):
    # next_url = ''
    # while next_url is not None:
    ## Run for 5 pages
    # HINT: use a for loop

        ## run through each result of the page
        # HINT: use a for loop

            ## Save the image of the result to the hard disk

            ## write the location and properties to the shapefile

        ## Get the url of the next page
        # HINT: look through the response dictionary for a link to the next page
        ## Request the next page

