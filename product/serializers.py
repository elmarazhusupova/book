from rest_framework import serializers
from .models import Book, Category, Author, CartItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'desc', 'author', 'category', 'slug', 'old_price', 'price']

    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'category_id', 'slug']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'user', 'books_name', 'quantity')

    # books_name = serializers.StringRelatedField()

    def to_representation(self, instance):
        rep = super(CartItemSerializer, self).to_representation(instance)
        rep['books_name'] = instance.books_name.name
        rep['user'] = instance.user.last_name
        return rep