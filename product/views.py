from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category


class BooksView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


