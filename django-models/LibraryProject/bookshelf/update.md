from bookshelf.models import Book  
updated_book = Book.objects.get(id=1)
updated_book.title = "Nineteen Eighty-Four"
updated_book.save()
print(f"{updated_book.title} by {updated_book.author} published in the year {updated_book.publication_year}")
#Expected Output : Nineteen Eighty-Four by George Orwell published in the year 1949