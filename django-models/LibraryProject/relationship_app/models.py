from django.db import models


class Author(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self) -> str:  # pragma: no cover - simple repr
		return self.name


class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

	def __str__(self) -> str:  # pragma: no cover - simple repr
		return f"{self.title} ({self.author})"


class Library(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="libraries", blank=True)

	def __str__(self) -> str:  # pragma: no cover - simple repr
		return self.name


class Librarian(models.Model):
	name = models.CharField(max_length=200)
	library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

	def __str__(self) -> str:  # pragma: no cover - simple repr
		return f"{self.name} — {self.library}"

