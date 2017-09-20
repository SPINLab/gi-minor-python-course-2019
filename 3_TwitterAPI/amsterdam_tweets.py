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

# To find the Amsterdam Twitter ID we use the reverse_geocode method of the tweepy
# API object. We need a latitude and longitude of Amsterdam for this.
places = api.reverse_geocode(lat=52.362951, lon=4.928977)
# this returns a list of places associated with the latitude and longitude given.
# Print the places and search for the amsterdam city place id. You will probably also
# find a neighborhood, the province of Noord-Holland and the country of the Netherlands
# in the list of places.
# We can see that the city of Amsterdam is the first in the list, so we save the first
# item in the list as a variable.
amsterdam = places[0]
# To get the id from this variable we use the folowing command:
amsterdam_id = amsterdam.id

# Create the query (search text) HINT: To search based on a Twitter place ID search for
# "place:`ID`", replacing `ID` with the ID found of the place.
# Since we saved the ID in the variable amsterdam_id we need to insert this variable
# into a string. HINT: Look at the recap to see how to put variables into strings.
# Check if the query works by entering it in the search bar on the twitter website:
# https://twitter.com/search-home
# You should see tweets located in Amsterdam
query = "place:{}".format(amsterdam_id)

# Create a tweepy cursor. A cursor is an object that points to other objects, which you
# can iterate through. In our case the cursor will point to the recent 1000 tweets
# located in Amsterdam. The cursor is build using tweepy.Cursor(api.method, args),
# where api.method is any method in the tweepy api object and args are the arguments
# that need to be passed into said method.
# HINT: Use the tweepy documentation online (http://docs.tweepy.org/en/v3.5.0/api.html) to find
# out which api method you need to search for tweets and which argument you have to use to pass in the query.
tweet_cursor = tweepy.Cursor(api.search, q=query).items(1000)

# To save all tweets with coordinates we loop through all and add the tweets with
# coordinates to a list.

tweets = []

for tweet in tweet_cursor:
    # We can convert the tweet to a dictionary using _json
    tweet_dict = tweet._json
    # HINT: Print a tweet dictionary, where is the location saved?
    # HINT: Use an if statement to check if the coordinates are present.
    if tweet_dict["coordinates"] is not None:
        # append the tweet to the lift if it has coordinates. Look at the recap to see
        # how to append a value to a list
        tweets.append(tweet_dict)


# Save to a shapefile using the fiona module similar to the previous assignment.
# Think about which information you want to save to the properties of each point.
# HINT: look in the tweet list and pick a tweet. Look in the dictionary which properties are available.
# Also think about the coordinate system we are using and adjust the crs accordingly if needed.

crs = from_epsg(4326)
schema = {'geometry': 'Point',
          'properties': {'Text': 'str',
                         'DateTime': 'str',
                         'User': 'str'}}

shp_filepath = 'tweet_locations_.shp'

with fiona.open(shp_filepath, 'w', 'ESRI Shapefile',
                schema=schema, crs=crs) as shp:

    for tweet in tweets:
        shp.write({'geometry': tweet["coordinates"],
                   'properties': {'Text': tweet["text"],
                                  'DateTime': tweet["created_at"],
                                  'User': tweet["user"]["name"]}})
