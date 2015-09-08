### Configuration

- install BeautifulSoup on your machine: open a command prompt in (Start Menu -> Run cmd...) and execute ```pip install --user BeautifulSoup4```

- download the data and examples: go to https://github.com/ndkv/vu-python and click Download ZIP (lower right corner)

- unzip the folder somewhere and navigate to ```vu-python\workshop-scraping```

- open and run ```scrape-example.py``` in Spyder to check whether everything is configured correctly

 ### Getting started

- get to know BeautifulSoup: open ```scrape-example.py```, uncomment the commented statements and run the script. Try to figure out what is going on. Study the used functions in the BeautifulSoup documentation (see below).

- change something in the source file ```library.html``` e.g. the title of the page or the title/author of the book with attribute ```id=1```, etc. and run ```scrape-example.py``` again. Are your changes reflected in the output?

### Warming up

- once you grasp what is going on, try to create a Comma-Separated Values (CSV) file that contains each book's title and author. HINT: find, fix and call ```extract_books``` function.

- open the file you created in Notepad/Excel to check whether everything worked fine.

- add an extra book in your source file (library.html) and run the code again. Is it added to your file? HINT: you can copy/paste one of the other books and change the ```title``` and ```author```


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/


#### Common BeautifulSoup operations

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
