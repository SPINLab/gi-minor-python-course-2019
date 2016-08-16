## Strings and Console Output

country = ";The Netherlands, NL"

# print "First letter is", country[1]
# print "Length of string is", len(country)

country = country + ", Europe"
# print "Welcome in %s, %s, %s you happy person" % (country, "bla bla", str(1))

# print "Welcome in " + country + " bla bla " + str(1) + " happy person"

# print country

bogus = ";"
country = country.replace(bogus,"")
# print country

# print country
places = country.split(", ")

# print places[0]

for place in country.split(", "):
	print place.upper()