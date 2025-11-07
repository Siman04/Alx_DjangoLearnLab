from django.urls import path
from . import views
from .views import list_books

app_name = "relationship_app"

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
