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

	class Meta:
		permissions = (
			('can_add_book', 'Can add book'),
			('can_change_book', 'Can change book'),
			('can_delete_book', 'Can delete book'),
		)


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


# Extend the built-in User model with a UserProfile to store roles
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
	ROLE_ADMIN = "Admin"
	ROLE_LIBRARIAN = "Librarian"
	ROLE_MEMBER = "Member"

	ROLE_CHOICES = (
		(ROLE_ADMIN, "Admin"),
		(ROLE_LIBRARIAN, "Librarian"),
		(ROLE_MEMBER, "Member"),
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

	def __str__(self) -> str:
		return f"{self.user.username} ({self.role})"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)


