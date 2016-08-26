from bs4 import BeautifulSoup
import codecs

with open('sources/windstats.htm', 'r') as f:
    data = BeautifulSoup(f)
 
rows = data.find_all('tr')

turbines_f = codecs.open('results/turbines.csv', 'w', encoding="utf8")
# turbines_f = open('results/turbines.csv', 'w')

turbines_f.write('turbine,fabrikant\n')
   
for row in rows:
    cells = row.find_all('td')

    if cells != []:
        print cells[0]

        turbines_f.write("%s,%s\n" % (cells[1].string, cells[2].string))

turbines_f.close()