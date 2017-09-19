## Strings and Console Output

country = ";The Netherlands, NL"

print "First letter is", country[1]
print "Length of string is", len(country)

country = country + ", Europe"
print country

dir(country)

bogus = ";"
country = country.replace(bogus, "")
# print country


places = country.split(", ")

print places[0]

for place in country.split(", "):
    print place.upper()


nl = "The Netherlands"
be = "Belgium"
EU_countries = 28

print "The EU has " + str(EU_countries) + " member countries, including " + nl + " and " + be
print "The EU has {2} member countries, including {0} and {1}".format(EU_countries, nl, be)
