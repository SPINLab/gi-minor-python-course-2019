import pandas as pd
import geopandas as gpd
from twython import Twython
from shapely.geometry import Point

# Consumer keys and access tokens, used for OAuth. Fill in your personal keys.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Create a Twython API object using the OAuth tokens:
api = Twython(consumer_key, consumer_secret,
                  access_token, access_token_secret)

# Test the connection
print(api.verify_credentials())

# To find the Amsterdam Twitter ID we use the reverse_geocode method of the twython
# API object. We need a latitude and longitude of Amsterdam for this.
# https://developer.twitter.com/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode.html
places = api.reverse_geocode(lat=???, long=???)

# this returns a list of places associated with the latitude and longitude given.
# Print the places and search for the amsterdam city place id. You will probably also
# find a neighborhood, the province of Noord-Holland and the country of the Netherlands
# in the list of places.
# We can see that the city of Amsterdam is the first in the list, so we save the first
# item in the list as a variable.
amsterdam = #???



# Save the ID found in the just created 'amsterdam' dictionary in a separate variable
amsterdam_id = #???



# Create the query (search text) HINT: To search based on a Twitter place ID search for
# "place:`ID`", replacing `ID` with the ID found of the place.
# Since we saved the ID in the variable amsterdam_id we need to insert this variable
# into a string. HINT: Look at the recap to see how to put variables into strings.
# Check if the query works by entering it in the search bar on the twitter website:
# https://twitter.com/search-home
# You should see tweets located in Amsterdam
query = #???


# The maximum amount of tweets returned by a twitter API request is 100.
# To get older tweets than the first 100 we need to use the max_id parameter,
# as described in the twitter API documentation:
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
# We can set the max_id to 1 less than the id of the last tweet we retrieved to retrieve
# a completely new set of tweets.
# So to get more and more new tweets we can create a loop, which at each iteration
# requests 100 tweets with a max_id of 1 less than the last tweet of the previous iteration.
###########################
# To make this loop work we first need to get the id of the latest tweet first.
# use the api.search method and the query we made before to request the latest tweet
# and save the 'id' if this tweet to a variable
latest_tweet = api.search(???)
last_id = #???


# Create a loop which, on each iteration, requests 100 new tweets. Let it loop for 10 iterations
# so that in the end we have about 1000 tweets (probably closer to 800 tweets, since the api does not always return the full 100 tweets requested).
# Save the retrieved tweets in a list.


tweets = []
for #???
    # hint: use api.search with our query to get 100 new tweets, set the count and max_id parameter accordingly

    # hint: instead of append, use the extend method to extend a list with another list (if we use append here we get a list of lists instead of 1 big list)

    # hint: at the end of each iteration of the loop update the last_id variable





# To save all tweets with coordinates we loop through all and add the tweets with
# coordinates to a list.
tweets_with_geo = []

for #???
    # HINT: Print (or look up in the variable explorer) a tweet dictionary, where is the location saved?
    # HINT: Use an if statement to check if the coordinates are present.
    if #???
        # append the tweet to the lift if it has coordinates. Look at the recap to see
        # how to append a value to a list




# We now need to create a GeoDataFrame with all the information we want to save.
# This GeoDataframe we can save as a shapefile, which we can import into ArcMap.
# Look at which information is in each tweet dictionary (via a print to console, or via the variable explorer).
# Think of which info we would like to save (maybe, for example: the text, username, etc),
# and what is not relevant to save with the shapefile (maybe, for example: retweeted status, favorite count, etc).
#######
# Create a new list, and loop through the tweets with a geotag. For each tweet create a new dictionary with
# only the relevant information in it and append it to the newly created list.
# Save the coordinates as a Point geometry object.
# hint: remember the previous exercise how to convert coordinates to a Point geometry object.
# hint: the same as in the previous exercise, the coordinates are in the wrong order for the creation of the Point geometry object, so reverse it.
tweets_filtered = []
for #???
    new_tweet = {}
    #???



# Create a DataFrame of the list of tweets:
tweets_df = pd.DataFrame(tweets_filtered)
# Create a GeoDataFrame of the DataFrame:
tweets_gdf = gpd.GeoDataFrame(tweets_df, geometry='geom')
# Save the GeoDataFrame to a shapefile:
tweets_gdf.to_file('tweets.shp')
# Import into ArcMap
