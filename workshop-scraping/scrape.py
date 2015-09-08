from bs4 import BeautifulSoup as BS

with open('library.html', 'r') as f:
	data = BS(f)

books_f = open('data/books.csv', 'w')
books_f.write('title,author\n')

for book in data.find_all(class_="book"):
	title = book.find(class_="title").text
	author = book.find(class_="author").text

	books_f.write("%s,%s\n" % (title, author))

books_f.close()


# for child in data.find(id="onloan").children:
# 	print child