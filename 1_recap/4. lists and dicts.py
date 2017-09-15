## Lists

cities = ["Rotterdam", "The Hague", "Amsterdam", "Utrecht"]


#print cities
#print cities[0]
#print cities.pop()
#print cities
#cities.pop(0)
#print cities

#chaos = ["Rotterdam", cities, [1, 2, 3, 4, [1, 2, 33]], "Amersfoort", 5]
#print chaos[2]

print chaos
for value in chaos
    print value

# print dir(chaos)


# print chaos



## Dicts

populations = {
	"Amsterdam": 80000,
	"Rotterdam": [12, 23],
	"The Hague": 100000
}

# print populations

# print populations["Amsterdam"]

# print populations

populations.update({
  	"Utrecht": 200000,
  	"Groningen": 300000
})

groningen_key = populations.keys()[0]

print populations[groningen_key]

populations.pop("Amsterdam")
print populations

print dir(populations)


print populations.values()
print 300000 in populations.values()

# NOTE: dictionaries are not ordered.



 # polygon = [[x,y], [x,y], [x,y]]



for populatie