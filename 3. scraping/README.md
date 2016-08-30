# Chapter 3. Scraping

Scraping is the act of automatically extracting structured data from (unstructured) web pages. 
 
 Suppose you want to map every windturbines in The Netherlands and analyse them as a whole. A quick search on Google will probably lead you to [windstats.nl](http://windstats.nl/turbines.php). This is a great resource! However, how are you going to obtain the data? There is no `download` button... Of course, you can send an email and ask for a copy but you'll need to do that every time the dataset changes. You could copy it by hand but let's be honest: you have better things to do.
    
Luckily there is a third option: write a Python script to do it for you!  

## Assignment

Task 1. You are asked to scrape the fictional library website contained in `library.html` 
 
 Task 2. You are asked to extract the windturbines and their properties from `windstats.htm`

## Introduction to BeautifulSoup

In this course we'll use the `BeautifulSoup` (BS) module to scrape web pages. `BS` is powerful and fairly straightforward (we hope) to learn due to its outstanding documentation.
 
 BeautifulSoup parses (= reads) a page and allows you to extract its components by calling BS functions. For example, to find all paragraphs in a web page you can search for the `<p>` element like so:

    from bs import BeautifulSoup
    
    with open('sources/windstats.htm', 'r') as f:
        soup = BeautifulSoup(f)
    
    soup.find_all("p")

BeautifulSoups' documentation is lives at [http://www.crummy.com/software/BeautifulSoup/bs4/doc/](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).

## Getting Started

1. get to know BeautifulSoup: open `scrape-example.py`, uncomment the commented statements and run the script. Try to figure out what is going on. Study the used functions in the BeautifulSoup documentation (see below).

2. change something in the source file `library.html` e.g. the title of the page or the title/author of the book with attribute `id=1`, etc. and run `scrape-example.py` again. Are your changes reflected in the output?

## Scrape your local library

- once you grasp what is going on, try to create a Comma-Separated Values (CSV) file that contains each book's title and author. HINT: find, fix and call `extract_books` function.

- open the file you created in Notepad/Excel to check whether everything worked fine.

- add an extra book in your source file (library.html) and run the code again. Is it added to your file? HINT: you can copy/paste one of the other books and change the `title` and `author`

## Scrape windstats

Once you've conquered `library.html` you can move on to `windstats.html`.


## Hints

- right click on an HTML element in Firefox -> Inspect element to see its HTML definition (tags and attributes)