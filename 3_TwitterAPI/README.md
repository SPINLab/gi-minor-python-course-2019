## Chapter 3. Twitter API

Another interesting API is the one from Twitter. Tweets can be a great source of information on range of topics. It has, for example, been used in [mapping natural disasters](http://www.ra.ethz.ch/CDStore/www2010/www/p851.pdf), [predicting the stock market](https://arxiv.org/pdf/1010.3003&), [mapping the aurora borealis](http://onlinelibrary.wiley.com/doi/10.1002/2015GL063709/full), [predicting election results](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM10/paper/viewFile/1441/1852), and [assessing public health](https://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/viewFile/2880/3264).

The twitter API can be used both for posting tweets and searching for tweets, as well as a range of other twitter features. Since we are interested in twitter data, the search function is what we are interested in. When searching for tweets the API is limited to recent messages. If historical data is required you would need to purchase it from an archive like [Gnip](https://gnip.com/historical/). A way to generate your own dataset would be to set up a listener, which will download tweets you are looking for as they get posted. The more time passes the bigger the dataset becomes. Since we don't have the time to set this up and wait for data to come in, today we are limited to recent tweets.

As before our research area is going to be Amsterdam. To be able to use tweets as geographical data we need tweets with a precise location. Sadly for us (but perhaps good for privacy) tweets only contain a precise location (geotag) if the user chooses to provide it. Consequently only a fraction of the tweets contain a latitude and longitude. Though even if they don't have a precise location the general area can be known, so tweets can be linked to Amsterdam without having this geotag. Consequently even if we limit ourselves to a geographical area like Amsterdam most tweets will not have a geotag. We will have to make do with the data available.

Because we are limited by time (only recent tweets), by location (only Amsterdam) and by the requirement of an available geotag, we have a limited number of usable tweets to work with. Consequently we can not further filter tweets by a subject (via a hashtag, for example). Therefore we have to keep this assignment more general. We will look how tweets are distributed over Amsterdam and if we can find some event by analysing the tweets (multiple people tweeting about the same thing).

The Twitter API is not an open API like the one from the Luchtmeetnet. It requires a Twitter account (that has joined Twitter Developer), and therefore when we use the API in python we need a way to identify ourselves. This is done using OAuth, a protocol for authorization, which is often used to grant applications access to information without using usernames and passwords. OAuth uses access tokens to verify the authenticity of the user making the requests.

We could use the `requests` module as we did with the Luchtmeetnet API, but it would require quite a bit of set up. Luckily there are modules made specifically for the Twitter API. One of those modules is `twython`, which is the library we are going to use today.

## Assignment Summary

Task 1. Setup a Twitter (Dev) account

Task 2. Setup API access through OAuth

Task 3. Use a cursor to retrieve tweets from Amsterdam with a geotag

Task 4. Export the tweets to a shapefile

Task 5. Do some spatial analysis in ArcMap

## Setting up a Twitter (Dev) account

1. Create Twitter account (if you do not already have one) and log in.

2. Go to https://developer.twitter.com and click `apply` in the top right corner.

3. Verify your phone number.

4. When asked for application text, you can use the following text we prepared:

> As a student Geographic Information Science/Systems I want to research the possibilities and opportunities to integrate twitter data in my spatial analysis framework. I am interested in spatial patterns and correlations. I aim to combine people's opinions with other spatial recourses like income, distance to nature, heritage and jobs.

5. Verify your email.

6. Create an app (`Create new app` -> `Create app`).

7. Fill in the fields. App name, description, and website can be whatever you want (can be gibberish). The Call URLs etc can be ignored and left empty. In the app usage field you can enter the following text:

> For educational and research purposes in the context of the Dutch national minor in Geographic Information Science.

8. Go to `Permissions` tab, press edit, and change access to `Read, Write and Access Direct Messages` and update the settings.

9. Go to `Keys & Tokens` tab and under `Consumer API keys` copy `API key` and `API secret` to a text file.

10. Press `Create` to create access tokens & copy `access token` and `access token secret` to a text file.

## Gain API access in python

1. Go to the [twython documentation](https://twython.readthedocs.io/en/latest/usage/basic_usage.html) and find out how to make twython gain access to the API.

2. Open `amsterdam_tweets.py` and create a twython API object with access to the API. Test the connection by using the verify_credentials method. The `.py` file contains pointers and hints to help you. Continue working in this file during the rest of this assignment. NOTE: If no access can be gained, regenerate all keys and try again.

## Retrieve the recent tweets in Amsterdam

1. Find out the Twitter place ID of Amsterdam. Use the `reverse_geocode` method of the twython API object.

2. Create the query (the search text) to get tweets from Amsterdam. HINT: To search based on a Twitter place ID search for "place:`ID`", replacing `ID` with the ID found of the place.

3. Create a loop which requests 100 tweets each iteration, using the max_id parameter to receive older and older tweets. See: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets

4. Loop through the tweets and save the tweets which have coordinates attached to it in a list.

## Export the tweets to a shapefile

1. Similar to previous assignment, use geopandas to create a point shapefile with the tweets. Think of which information to save in the attribute table.

## Spatial analysis in ArcMap

1. Import the shapefile into ArcMap.

2. Explore the data.

3. Can you find some events or accidents happening in Amsterdam recently?

4. How are the tweets distributed over Amsterdam? Can you make some maps to visualize the distribution?

5. Can you explain the distribution you found?
