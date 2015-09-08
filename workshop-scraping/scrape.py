from bs4 import BeautifulSoup

with open('sources/windstats.htm', 'r') as f:
	data = BeautifulSoup(f)
 
print data