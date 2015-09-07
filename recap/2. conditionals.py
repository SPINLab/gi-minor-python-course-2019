# Conditionals and Control flow


# if condition:
# 	do something
# else: 
# 	do something else



country = "The Netherlands"

if country == "The Netherlands":
	print country
else:
	print "Does not satisfy if condition."



continent = "Europe"

if country == "The Netherlands" and continent == "Europe":
	print country, continent
else:
	print "Does not satisfy if condition."



country = "Spain"

if country == "The Netherlands" or continent == "Europe":
	print country, continent
else:
	print "Does not satisfy if condition."