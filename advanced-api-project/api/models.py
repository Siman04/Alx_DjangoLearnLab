from django.db import models


class Author(models.Model):
    """Author model stores a name for the author."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model stores title, publication_year, and a foreign key to Author.

    Permissions and relationships:
    - Each Book links to an Author via a ForeignKey establishing a one-to-many
      relationship from Author to Book.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
