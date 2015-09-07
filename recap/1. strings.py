## Strings and Console Output
# Code Academy material




country = " The Netherlands, NL"

print "First letter is", country[1]
print "Length of string is", len(country)

country = country + ", Europe"
print "Welcome in %s" % country

# Useful tidbits

print country
country = country.strip(" ")
print country

print country.split(",")