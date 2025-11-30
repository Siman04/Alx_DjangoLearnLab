from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookDetailAPIView,
    CreateView,
    UpdateView,
    DeleteView,
)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/create', CreateView.as_view(), name='book-create'),
    path('books/update', UpdateView.as_view(), name='book-update'),
    path('books/delete', DeleteView.as_view(), name='book-delete'),
]
