from django.urls import path, include
from rest_framework import routers
from .views import CartItemView, BooksView, AuthorView, CategoriesView
from . import views

router = routers.DefaultRouter()
router.register(r'book', BooksView)
router.register(r'author', AuthorView)
router.register(r'category', CategoriesView)
# router.register(r'items', ItemView)
router.register(r'cart', CartItemView, basename='cart')


urlpatterns = [
    path('', include(router.urls)),
    path('cart/<int:pk>', views.CartItemView.as_view({'get': 'cart_item'}), name='cart_item'),
]
