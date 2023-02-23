from django.urls import path, include
from rest_framework import routers
from .views import CartItemView, BooksView, AuthorView, CategoriesView
from . import views
from accounts.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'book', BooksView)
router.register(r'author', AuthorView)
router.register(r'category', CategoriesView)
router.register(r'cart', CartItemView, basename='cart')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/<int:pk>', views.CartItemView.as_view({'get': 'cart_item'}), name='add_to_cart'),
]
