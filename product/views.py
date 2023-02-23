from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer
from .models import Book, Category, Author
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from django.shortcuts import get_object_or_404


class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['author__first_name', 'author__last_name', 'category__title', 'name']
    pagination_class = PageNumberPagination


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        # cart = get_object_or_404(Book, pk=id)
        user = request.user
        book_id = request.data.get('id')
        quantity = request.data.get('quantity', 1)
        book = Book.objects.get_object_or_404(Book, id=book_id)
        book_name, created = CartItem.objects.get_or_create(user=user, book=book)
        if not created:
            book_name.quantity += int(quantity)
            book_name.save()
        return Response(self.get_serializer(book_name).data)

    @action(detail=False, methods=['post'])
    def remove_from_cart(self, request):
        user = request.user
        book_id = request.data.get('book.id')
        book = CartItem.objects.get(id=book_id)
        cart_item = CartItem.objects.get(user=user, book=book)
        cart_item.delete()
        return Response({'message': 'Item removed from cart.'})

