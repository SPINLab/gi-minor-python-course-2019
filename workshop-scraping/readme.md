### Configuration

 - install BeautifulSoup on your machine: open a command prompt in Windows (Start Menu -> Run cmd...) and execute

     pip install --user BeautifulSoup4

 - download the data and examples: go to https://github.com/ndkv/vu-python and click Download ZIP (lower right corner)

 - unzip the folder and open scrape-example.py in Spyder

 - run scrape-example.py once to check whether everything is configured correctly

 ### Getting started

  - run and investigate scrape.example.py: uncomment the commented lines in scrape-example.py and try to figure out what is going on. Try to find the used functions in the BeautifulSoup documentation (see below).

 - once you grasp what is going on, try to create a Comma-Separated Values (CSV) file that contains each book's title and author.


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/


#### Common BeautifulSoup operations operations

Find all tags of type ```p```

    soup.find_all("p")

### Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)