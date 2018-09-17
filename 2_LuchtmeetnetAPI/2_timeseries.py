import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Choose a station number (e.g. the number of the amsterdam station of the previous exercise) and save to a variable




# Choose a chemical compound and request the data (no need to specify a page yet, you will by default recieve the most recent page)
# Create a dictionary of the response like in the previous exercise.
# hint: you need to specify the station number in the URL
# hint: you need to specify the chemical compound in the parameters of the request (http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
# hint: look in the API documentation what the parameter to define a chemical compound is called (https://documenter.getpostman.com/view/1562017/RVnbBxf9)





# Create a list of values of the measured quantity of the chosen chemical compound and
# Create a list of corresponding timestamps
# hint: look in the data where the measured quantities and timestamps are stored
# hint: you will need to loop over the retrieved data
# hint: create empty lists and append the data to the lists in the loop (look back in the recap if you forgot how to append an item to a list)





# note that the timestamps are strings that are build a certain way (a format)
# we need to tell the computer how to interpret this string
# and create a datetime object with it that python can interpret
# before we can plot the data
# https://pymotw.com/2/datetime/#formatting-and-parsing
# For simplicity we give you the correct time format (but please try to understand it):
time_format = '%Y-%m-%dT%H:%M:%S+00:00'

# Change the loop so that the timestamp information is parsed using the format (https://pymotw.com/2/datetime/#formatting-and-parsing)





# Now plot the data using matplotlib
# https://pythonspot.com/plot-time-with-matplotlib/





# In the plot we can see it only spans a pretty limited timespan.
# To increase this we need to retrieve more pages of data (e.g. 10 pages)
# hint: use the 'page' parameter to define which page you want to request (http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
# hint: we now need to pass two parameters with the request (chemical compund and page number)
# hint: use a loop to request multiple pages
# hint: first create the empty lists again and then append the data in the loop
# hint: you can create a loop within a loop




# plot it





# it might be that the graph looks wrong in some places now
# this is due the data not being sorted by date
# to sort the data by date we are going to create a DataFrame using the pandas module
# a DataFrame is a datatype that stores tabular data, kinda like an excel sheet
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
# We will initaite a DataFrame:
df = pd.DataFrame()
# And then save the lists to columns in the DatFrame
df['timestamps'] = timestamps
df['values'] = values

# now that the data is in a DataFrame we can use the sort_values function of the DataFrame to sort the values by the timestamps
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html





# pandas DataFrames also come with easy function to make a plot, use it to create a plot of the sorted data
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html





# Save the DataFrame to a csv.
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html
df.to_csv('timeseries.csv')
