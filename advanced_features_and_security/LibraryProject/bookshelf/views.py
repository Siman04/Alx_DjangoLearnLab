from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Enforce can_view permission
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Enforce can_create permission
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # ...create logic here...
    return render(request, 'bookshelf/form_example.html')

# Enforce can_edit permission
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # ...edit logic here...
    return render(request, 'bookshelf/form_example.html', {'book': book})

# Enforce can_delete permission
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # ...delete logic here...
    return redirect('book_list')
