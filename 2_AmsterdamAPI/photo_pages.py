import requests
import fiona
from fiona.crs import from_epsg


# Request the first page of the 2016 directory of the API. And create a dictionary from it.








# open (create) a shapefile. Look at the previous exercise how to define the
# schema and crs, and create a shapefile with fiona using the schema and crs.

crs =


schema =



shp_filepath =



with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:


    ## Run for, for example, 5 pages
    # HINT: use a for loop. Look at the recap how to create a for loop.
    # HINT: use the range(*) function to create a list to loop through. * is the number.

    for ...?



        ## run through each result of the page
        # HINT: use a for loop. Again look at the recap to see how to loop through a list


        for ...?


            ## Save the image of the result to the hard disk. Like we did in previous exercises.




            ## write the location and properties to the shapefile. Like we did in previous exercises.

            shp.write(...?



        ## Get the url of the next page
        # HINT: look through the response dictionary for a link to the next page



        ## Request the next page using the requests module. And create a dictionary from it.



## IMPORTANT: INDENTATION! The 'with' and 'for' loops use indentation.
