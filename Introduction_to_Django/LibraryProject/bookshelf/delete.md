from bookshelf.models import Book  
book = Book.objects.get(id=1)
book.delete()

books = Book.objects.all()
for book in books:
	print(f"{book.title} by {book.author} published in the year {book.publication_year}")
#Expected Output : (1, {'bookshelf.Book': 1})