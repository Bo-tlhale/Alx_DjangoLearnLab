#Queries
#Books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)

#List all the books of a library
library = Library.objects.get(name="City Library")
books_in_library = library.books.all()

#Retrieve the librarian for a library
library = Library.objects.get(name="City Library")
librarian = library.librarian