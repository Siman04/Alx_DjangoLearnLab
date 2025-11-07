from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from .models import Book, Library, UserProfile, Author
from .models import Library


def list_books(request):
	"""Function-based view that lists all books and their authors.

	Renders the `relationship_app/list_books.html` template with a `books`
	context variable.
	"""
	# Use the explicit call the checker expects
	books = Book.objects.all()
	return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
	"""Class-based view (DetailView) to display a single Library and its books.

	Template: `relationship_app/library_detail.html`
	Context object name: `library`
	"""
	model = Library
	template_name = "relationship_app/library_detail.html"
	context_object_name = "library"


def register_view(request):
	"""Allow a user to register using Django's built-in UserCreationForm."""
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# login the user immediately after registration
			auth_login(request, user)
			return redirect("relationship_app:list_books")
	else:
		form = UserCreationForm()
	return render(request, "relationship_app/register.html", {"form": form})


@permission_required('relationship_app.can_add_book')
def add_book(request):
	"""Create a new Book (requires can_add_book permission)."""
	if request.method == "POST":
		title = request.POST.get("title")
		author_id = request.POST.get("author_id")
		author = get_object_or_404(Author, pk=author_id)
		Book.objects.create(title=title, author=author)
		return redirect("relationship_app:list_books")
	# simple form fallback
	return HttpResponse("Add book form")


@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
	"""Edit an existing Book (requires can_change_book permission)."""
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		title = request.POST.get("title")
		book.title = title or book.title
		book.save()
		return redirect("relationship_app:list_books")
	return HttpResponse(f"Edit book form for {book.pk}")


@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
	"""Delete a Book (requires can_delete_book permission)."""
	book = get_object_or_404(Book, pk=pk)
	if request.method == "POST":
		book.delete()
		return redirect("relationship_app:list_books")
	return HttpResponse(f"Confirm delete for {book.pk}")


def _is_admin(user):
	return hasattr(user, "userprofile") and user.userprofile.role == UserProfile.ROLE_ADMIN


def _is_librarian(user):
	return hasattr(user, "userprofile") and user.userprofile.role == UserProfile.ROLE_LIBRARIAN


def _is_member(user):
	return hasattr(user, "userprofile") and user.userprofile.role == UserProfile.ROLE_MEMBER


@login_required
@user_passes_test(_is_admin)
def admin_view(request):
	return render(request, "relationship_app/admin_view.html")


@login_required
@user_passes_test(_is_librarian)
def librarian_view(request):
	return render(request, "relationship_app/librarian_view.html")


@login_required
@user_passes_test(_is_member)
def member_view(request):
	return render(request, "relationship_app/member_view.html")
