import uuid
from django.db import models
from accounts.models import User


class Publisher(models.Model):
    title = models.CharField(max_length=255)
    books = models.ForeignKey('Book', on_delete=models.CASCADE, blank=False, null=False, related_name='books')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    books = models.ForeignKey('Book', on_delete=models.CASCADE, blank=True, null=True, related_name='book')

    def __str__(self):
        return self.last_name


class Category(models.Model):
    title = models.CharField(max_length=200)
    category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    slug = models.SlugField(default=None)

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True, related_name='author')
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='category')
    price = models.FloatField()
    new_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField(default=None, blank=True, null=True)
    published_day = models.DateField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, blank=True, null=True, related_name='publisher')
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    books_name = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.user)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
