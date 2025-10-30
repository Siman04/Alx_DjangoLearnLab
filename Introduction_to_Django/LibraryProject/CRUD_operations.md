# --- 1. Create Operation ---
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# --- 2. Retrieve Operation ---
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# --- 3. Update Operation ---
book.title = "Nineteen Eighty-Four"
book.save()
# Check the update
Book.objects.get(pk=book.pk).title

# --- 4. Delete Operation ---
book.delete()
Book.objects.all()