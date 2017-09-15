import tweepy
import fiona
from fiona.crs import from_epsg

# Consumer keys and access tokens, used for OAuth. Fill in your personal keys.
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Create an OAuth authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a tweepy API object, using the OAuth object
api = tweepy.API(auth)

# Test the connection
user = api.me()
print 'Logged in as {}'.format(user.name)

# Search for Amsterdam Twitter ID. Use the reverse_geocode method of the tweepy
# API object. You will need a latitude and longitude of Amsterdam for this.
places = api.reverse_geocode(lat=52.362951, lon=4.928977)
# Print the places and search for the amsterdam city place id. You will probably also
# find a neighborhood, the province of Noord-Holland and the country of the Netherlands
# in the list of places.
amsterdam = places[0]
amsterdam_id = amsterdam.id

# Create the query (search text) HINT: To search based on a Twitter place ID search for
# "place:`ID`", replacing `ID` with the ID found of the place.
# Check if the query works by entering it in the search bar on the twitter website:
# https://twitter.com/search-home
# You should see tweets located in Amsterdam
query = "place:{}".format(amsterdam_id)

# Create a tweepy cursor. A cursor is an object that points to other objects, which you
# can iterate through. In our case the cursor will point to the recent 1000 tweets
# located in Amsterdam. The cursor is build using tweepy.Cursor(api_method, args),
# where api_method is any method in the tweepy api object and args are the arguments
# that need to be passed into said method.
# HINT: Use the dir or help function in python or the tweepy documentation online to find
# out which method you need and which argument you have to use to pass in the query.
tweet_cursor = tweepy.Cursor(api.search, q=query).items(1000)

# To save all tweets with coordinates we loop through all and add the tweets with
# coordinates to a list.
tweets = []
for t in tweet_cursor:
    # HINT: Print a tweet, where is the location saved?
    # HINT: Use an if statement to check if the coordinates are present.
    if t.coordinates is not None:
        tweets.append(t)

# Save to a shapefile using the fiona module similar to the previous assignment.
# Think about which information you want to save to the properties of each point.
# HINT: print a tweet and have a look which properties are available.
# Also think about the coordinate system we are using and adjust the crs
# accordingly if needed.
crs = from_epsg(4326)
schema = {'geometry': 'Point',
          'properties': {'Text': 'str',
                         'DateTime': 'datetime',
                         'User': 'str'}}

shp_filepath = 'Data\\tweet_locations_06_09.shp'

with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:

    for t in tweets:
        shp.write({'geometry': t.coordinates,
                   'properties': {'Text': t.text,
                                  'DateTime': t.created_at,
                                  'User': t.user.name}})
