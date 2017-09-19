## Loops

for variable in list/dict/string/file:
    do something with variable


country = "The Netherlands"

for c in country:
    print c


cities = ["Rotterdam", "The Hague", "Amsterdam", "Utrecht"]

for item in cities:
    print item


for index in range(0, len(cities)):
    print index, cities[index]


for index, city in enumerate(cities):
    print index, city


populations = { "Amsterdam": 80000, "Rotterdam": 500000, "The Hague": 100000}

for key in populations:
    print key
    print populations[key]



# open file and iterate through contents
