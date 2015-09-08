### Configuration

- install BeautifulSoup on your machine: open a command prompt in Windows (Start Menu -> Run cmd...) and execute

```pip install --user BeautifulSoup4```

- download the data and examples: go to https://github.com/ndkv/vu-python and click Download ZIP (lower right corner)

- unzip the folder and open ```scrape-example.py``` in Spyder

- run scrape-example.py once to check whether everything is configured correctly

 ### Getting started

- run and investigate ```scrape-example.py```: uncomment the commented lines and try to figure out what is going on. Study the used functions in the BeautifulSoup documentation (see below).

- change something in the source file (i.e. library.html) e.g. the title of the page or a book, etc. and run ```scrape-example.py``` again. Are your changes reflected in the output?

### Warming up

- once you grasp what is going on, try to create a Comma-Separated Values (CSV) file that contains each book's title and author. HINT: find and fix the ```extract_books``` function.

- open the file you created in Notepad/Excel to check whether everything worked fine.

- add an extra book in your source file (library.html) and run the code again. Is it added to your file?


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/


#### Common BeautifulSoup operations operations

Find all tags of type ```p```

    soup.find_all("p")

### Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)### Configuration

- install BeautifulSoup on your machine: open a command prompt in Windows (Start Menu -> Run cmd...) and execute

    ```pip install --user BeautifulSoup4```

- download the data and examples: go to https://github.com/ndkv/vu-python and click Download ZIP (lower richt corner)

- unzip the folder and open scrape.py in Spyder


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#contents-and-children


#### Common BeautifulSoup operations operations

Find all tags of type ```p```

    soup.find_all("p")

### Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)
