# Chapter 3. Scraping

Scraping is the act of automatically extracting structured data from web pages. 
 
 Suppose you want to map and analyse all the windturbines in The Netherlands. And quick search on Google will probably lead you to [windstats.nl](http://windstats.nl/turbines.php). This is a great resource! However, how are you going to obtain the data? There is no `download` button... Of course, you can send an email and ask for a copy but you'll need to do that every time the dataset changes. Copying this by hand is out of the question: you have better things to do. 
    
The most efficient way of obtaining this data is by writing a Python script to do it for you!  

## Assignment

Task 1. You are asked to scrape the fictional library website contained in `library.html` 
 
 Task 2. You are asked to extract the windturbines and their properties from `windstats.htm`

## Getting started

In this course we'll use the `BeautifulSoup` module to scrape web pages. `BS` is powerful and fairly straightforward (we hope) to learn due to its outstanding documentation. 

1. get to know BeautifulSoup: open `scrape-example.py`, uncomment the commented statements and run the script. Try to figure out what is going on. Study the used functions in the BeautifulSoup documentation (see below).

2. change something in the source file `library.html` e.g. the title of the page or the title/author of the book with attribute `id=1`, etc. and run `scrape-example.py` again. Are your changes reflected in the output?

### Warming up

- once you grasp what is going on, try to create a Comma-Separated Values (CSV) file that contains each book's title and author. HINT: find, fix and call `extract_books` function.

- open the file you created in Notepad/Excel to check whether everything worked fine.

- add an extra book in your source file (library.html) and run the code again. Is it added to your file? HINT: you can copy/paste one of the other books and change the `title` and `author`


### Working with BeautifulSoup

Documentation: http://www.crummy.com/software/BeautifulSoup/bs4/doc/


#### Common BeautifulSoup operations

Find all tags of type `p`

    soup.find_all("p")

### Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)