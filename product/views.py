from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def books(request):
    if request.method == "GET":
        product = Book.objects.all()
        serializer = BookSerializer(product, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def book(request, *args, **kwargs):
    pk = kwargs.get('pk')
    product = get_object_or_404(Book, id=pk)
    if request.method == "GET":
        serializer = BookSerializer(product)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def api_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view()
def api_category(request, pk):
    category = get_object_or_404(Category, category_id=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)