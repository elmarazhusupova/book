from rest_framework import serializers
from .models import Book, Category


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'desc', 'author', 'category', 'slug', 'old_price', 'price']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'category_id', 'slug']
