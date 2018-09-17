# Conditionals and Control flow

# if condition:
#     do something
# else:
#     do something


country = "Italy"

if country == "The Netherlands":
    print(country)
else:
    print("Does not satisfy if condition.")

if country == "The Netherlands":
    print("Nederland")
elif country == "Spain":
    print("Spanje")
elif country == "Italy":
    print("Italië")
else:
    print("Does not satisfy any of the conditions.")


continent = "Europe"

if country == "Italy" and continent == "Europe":
    print(country, continent)
else:
    print("Does not satisfy if condition.")



# country = "Spain"

# if country == "The Netherlands" or continent == "Europe":
# 	print(country, continent)
# else:
# 	print("Does not satisfy if condition.")

if True:
    print("Hallo")
