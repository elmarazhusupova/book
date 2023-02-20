from django_filters.rest_framework import FilterSet
from .models import Book


class ProductFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'author': ['exact'],
            'category': ['exact']
        }
