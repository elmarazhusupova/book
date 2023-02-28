from django.urls import path, include
from rest_framework import routers
from .views import CartItemView, AuthorView, CategoriesView, PublisherView, FeedbackView, BookView
from . import views
from .views import FavoriteBookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookView)
router.register(r'author', AuthorView)
router.register(r'category', CategoriesView)
router.register(r'cart', CartItemView, basename='cart')
router.register(r'publisher', PublisherView)
router.register(r'favorite_books', FavoriteBookViewSet, basename='favorite_books')
router.register(r'feedback', FeedbackView)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/<int:pk>/', views.CartItemView.as_view({'get': 'cart_item'}), name='add_to_cart'),
]

