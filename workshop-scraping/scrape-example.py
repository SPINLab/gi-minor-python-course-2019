from bs4 import BeautifulSoup

with open('source/library.html', 'r') as f:
	data = BeautifulSoup(f)
 
print data

#print data.title
#print data.title.string

#print data.title.parent.name

#print data.find_all('div')
#print data.find(id="book1")

#def extract_books():
#    books_f = open('data/books.csv', 'w')
#    books_f.write('title,author\n')
#    
#    for book in data.findAll(class_="book"):
#    	title = book.find(class_="title").text
#    	author = book.find(class_="author").text
#    
#    	books_f.write("%s,%s\n" % (title, author))
#    
#    books_f.close()

# for child in data.find(id="onloan").children:
# 	print child