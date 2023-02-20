from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer
from .models import Book, Category, Author
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class BooksView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['author__first_name', 'author__last_name', 'category__title']


class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
