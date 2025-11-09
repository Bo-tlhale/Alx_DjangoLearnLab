from bookshelf.models import Book  
book = Book.objects.get(title="1949")
print(f"{book.title} by {book.author} published in the year {book.publication_year}")
#Expected Output : 1984 by George Orwell published in the year 1949