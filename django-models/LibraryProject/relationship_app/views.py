from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView

from .models import Book, Library


def list_books(request):
	"""Function-based view that lists all books and their authors.

	Renders the `relationship_app/list_books.html` template with a `books`
	context variable.
	"""
	books = Book.objects.select_related("author").all()
	return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
	"""Class-based view (DetailView) to display a single Library and its books.

	Template: `relationship_app/library_detail.html`
	Context object name: `library`
	"""
	model = Library
	template_name = "relationship_app/library_detail.html"
	context_object_name = "library"
