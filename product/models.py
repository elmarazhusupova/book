import uuid
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    # books = models.ForeignKey(Product, )

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200)
    category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    slug = models.SlugField(default=None)
    # featured_product = models.OneToOneField('Product', on_delete=models.CASCADE, blank=True, null=True, related_name='featured_product')

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True, related_name='author')
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='category')
    discount = models.BooleanField(default=False)
    old_price = models.FloatField(default=100.00)
    slug = models.SlugField(default=None)

    @property
    def price(self):
        if self.discount:
            new_price = self.old_price - ((30/100)*self.old_price)
        else:
            new_price = self.old_price
        return new_price

    def __str__(self):
        return self.name
