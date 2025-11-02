from bookshelf.models import Book  
books = Book.objects.all()
for book in books:
	print(f"{book.title} by {book.author} published in the year {book.publication_year}")
#Expected Output : 1984 by George Orwell published in the year 1949