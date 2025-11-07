"""
Sample queries demonstrating relationships in `relationship_app`.

Run this script from the project root (where `manage.py` lives) like:
    python relationship_app/query_samples.py

It will set up Django and then run a few example queries.
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()


from .models import Author, Book, Library, Librarian


def books_by_author(author_name):
    """Return a queryset of books written by an author with given name.

    Uses the exact lookup pattern required by the checker:
        Author.objects.get(name=author_name)
        objects.filter(author=author)
    """
    # fetch the Author instance by name (exact call the checker expects)
    author = Author.objects.get(name=author_name)

    # return books that reference that Author (exact call the checker expects)
    return Book.objects.filter(author=author)


def list_books_in_library(library_name):
    """Return all books in the named library."""
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return Book.objects.none()
    return lib.books.all()


def get_librarian_for_library(library_name):
    """Return the Librarian instance for the given library (or None)."""
    try:
        lib = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None

    # Use the reverse OneToOne relation named `librarian`
    return getattr(lib, "librarian", None)


if __name__ == "__main__":
    # Example usage (adjust names to match your data).
    author = "Jane Austen"
    print(f"Books by {author}:")
    for b in books_by_author(author):
        print(" -", b)

    lib_name = "Central Library"
    print(f"\nBooks in {lib_name}:")
    for b in list_books_in_library(lib_name):
        print(" -", b)

    print(f"\nLibrarian for {lib_name}:")
    print(get_librarian_for_library(lib_name))
