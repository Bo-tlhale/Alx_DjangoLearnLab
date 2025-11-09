#Queries
#Books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

#List all the books of a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

#Retrieve the librarian for a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(librarian.name)