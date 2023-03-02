from django.urls import include, path
from accounts.views import UserCreate, LoginView


urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('login/', LoginView.as_view()),
]
