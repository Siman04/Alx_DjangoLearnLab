# --- 3. Update Operation ---
book.title = "Nineteen Eighty-Four"
book.save()
# Check the update
Book.objects.get(pk=book.pk).title
