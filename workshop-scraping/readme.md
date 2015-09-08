### Configuration

 - install BeautifulSoup on your machine: open a command prompt in Windows (Start Menu -> Run cmd...) and execute

     pip install --user BeautifulSoup4

 - download the data and examples: go to https://github.com/ndkv/vu-python and click Download ZIP (lower right corner)

 - unzip the folder and open scrape.py in Spyder

 - run scrape.py once to check whether everything is configured correctly


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/


#### Common BeautifulSoup operations operations

Find all tags of type ```p```

    soup.find_all("p")

### Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)