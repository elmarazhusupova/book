from .models import Book, Category, Author, Publisher, Feedback, Cart, FavoriteBook
from rest_framework import serializers


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'category_id', 'slug']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'image', 'price')


class FavoriteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteBook
        fields = ['id', 'book']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CartSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Cart
        fields = ('id', 'book', 'quantity')

    def create(self, validated_data):
        user = self.context['request'].user
        book_data = validated_data.pop('book')
        book = Book.objects.get(id=book_data['id'])
        cart, created = Cart.objects.get_or_create(user=user, book=book, defaults={'quantity': validated_data['quantity']})
        if not created:
            cart.quantity += validated_data['quantity']
            cart.save()
        return cart


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
