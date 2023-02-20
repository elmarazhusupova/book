from rest_framework import serializers
from .models import Book, Category, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'desc', 'author', 'category', 'slug', 'old_price', 'price']

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        rep['category'] = instance.category.title
        rep['author'] = f'{instance.author.last_name} {instance.author.first_name}'
        return rep



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'category_id', 'slug']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'last_name']
