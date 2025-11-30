from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Author 1')
        self.book = Book.objects.create(title='Book 1', publication_year=2000, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure response includes serialized data
        self.assertIsNotNone(response.data)

    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'publication_year': 2020, 'author': self.author.id}
        response = self.client.post(url, data)
        self.assertIn(response.status_code, (status.HTTP_201_CREATED, status.HTTP_403_FORBIDDEN))

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated', 'publication_year': 2001, 'author': self.author.id}
        response = self.client.put(url, data)
        self.assertIn(response.status_code, (status.HTTP_200_OK, status.HTTP_403_FORBIDDEN))

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertIn(response.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN))
