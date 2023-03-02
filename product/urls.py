from django.urls import path, include
from rest_framework import routers
from .views import CartView, AuthorView, CategoriesView, PublisherView, FeedbackView, BookView
from . import views

router = routers.DefaultRouter()
router.register(r'books', BookView)
router.register(r'author', AuthorView)
router.register(r'category', CategoriesView)
router.register(r'cart', CartView, basename='cart')
router.register(r'publisher', PublisherView)
router.register(r'feedback', FeedbackView)

urlpatterns = [
    path('', include(router.urls)),
    # path('cart/<int:pk>/', views.CartItemView.as_view({'get': 'cart_item'}), name='add_to_cart'),
]

