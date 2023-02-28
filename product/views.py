from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from .serializers import CategorySerializer, AuthorSerializer, CartItemSerializer, \
    PublisherSerializer, FavoriteBookSerializer, FeedbackSerializer, BookSerializer, BookListSerializer
from .models import Book, Category, Author, CartItem, Publisher, FavoriteBook, Feedback
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status, generics


class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherView(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['author__first_name', 'author__last_name', 'category__title', 'name']
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return self.serializer_class


class FavoriteBookViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteBook.objects.filter(user=self.request.user)


class CartItemView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        user = request.user
        book_id = request.data.get('id')

        book = Book.objects.get(id=book_id, user=user)
        book_name, created = CartItem.objects.get_or_create(user=user, book=book)
        if not created:
            book_name.save()
        return Response(self.get_serializer(book_name).data)

    # def create(self, request, *args, **kwargs):
    #     book_id = request.data.get('id')
    #     quantity = request.data.get('quantity')
    #     user = request.user
    #
    #     cart_item = CartItem.objects.filter(user=user).first()
    #     if cart_item:
    #         # cart_item.quantity += quantity
    #         cart_item.save()
    #     else:
    #         cart_item = CartItem.objects.create(user=user, book_id=book_id, quantity=quantity)
    #
    #     serializer = self.get_serializer(cart_item)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def remove_from_cart(self, request):
        user = request.user
        book_id = request.data.get('book.id')
        book = CartItem.objects.get(id=book_id)
        cart_item = CartItem.objects.get(user=user, book=book)
        cart_item.delete()
        return Response({'message': 'Item removed from cart.'})


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
