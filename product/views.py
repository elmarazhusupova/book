from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from .serializers import CategorySerializer, AuthorSerializer, \
    PublisherSerializer, FavoriteBookSerializer, FeedbackSerializer, BookSerializer, BookListSerializer, CartSerializer
from .models import Book, Category, Author, Publisher, FavoriteBook, Feedback, Cart
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


class CartViewSet(viewsets.ViewSet):
    serializer_class = CartSerializer

    def list(self, request):
        queryset = Cart.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Cart.objects.filter(user=request.user, id=pk)
        if queryset.exists():
            serializer = self.serializer_class(queryset.first())
            return Response(serializer.data)
        else:
            return Response({'detail': 'Not found.'}, status=404)


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
