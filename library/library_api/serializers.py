from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 'publication_year',
            'genre', 'category', 'publisher', 'cover_image', 'book_file'
        ]
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.full_name', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 'publication_year',
            'genre', 'category', 'publisher', 'cover_image', 'book_file'
        ]

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'biography', 'books']
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'full_name', 'biography', 'books']