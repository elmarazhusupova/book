from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books', views.books),
    path("api/book/<str:pk>", views.book),
    path("api/categories", views.api_categories),
    path("api/categories/<str:pk>", views.api_category)
]
