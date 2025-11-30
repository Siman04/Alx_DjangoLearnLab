from rest_framework import serializers
from .models import Book, Author
import datetime


class BookSerializer(serializers.ModelSerializer):
    """Serializes Book instances and validates publication_year."""

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure publication_year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError('publication_year cannot be in the future')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author instances and nests BookSerializer for related books."""

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
