import requests
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


# Start a pandas DataFrame
df = #???



# Start a list to save each found station number to



# To retrieve data from all stations we need to get all the station numbers.
# In the API documentation (https://documenter.getpostman.com/view/1562017/RVnbBxf9) find the URL to retrieve station numbers.
# Check how many pages there are and create a loop which goes from 1 to the total number of pages.
# Inside the loop retrieve the stations data of that page.
# Loop over that data.
# Save the station numbers to the earlier created list.





# Save the list in a column of the DataFrame




# Start a list to save the station coordinates to.


# Look in the API documentation for the url to retrieve information of a station.
# Loop over all station numbers found previously and use the url to retrieve information of each station.
# Look in the data of a station where to find the coordinates.
# Save each station's coordinates.
# note: the coordinates returned by the API are in the wrong order (at least for the shapely Point class which we will use later)
# You can reverse a list as such:  some_list[::-1]





# Save the coordinate list to a column in the DataFrame




# We will now create Point geometries from the coordinate data
# http://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
df['geom'] = #???




# to convert this regular DataFrame to a GeoDataFrame we need tell GeoPandas in which column the geometry is located
# http://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
gdf = #???

# Geopandas makes it easy to create a simple plot
# example:
nederland = gpd.read_file('./shp/nederland.shp')
base = nederland.plot()
gdf.plot(ax=base, color='red')
plt.show()

# We will now try to color the points based on the measured value of a chemical compound.
# Chose a chemical compound like before.
# Start a list to save found values to.



# Loop over all stations like before.
# Look in the API documentation how to request the measurements of a station.
# From each station save the latest measurement to the created list.
# If the station has no measurements for your selected compound append a 'float('nan')' to the list.





# Save the list to a column in the GeoDataFrame
gdf['value'] = #????

# Plot using geopandas:
base = nederland.plot()
gdf.dropna().plot(ax=base, column='value', scheme='Fisher_Jenks', k=20, cmap='YlOrRd')
plt.show()

# Save to a shapefile:
gdf.to_file('./shp/measurements.shp')