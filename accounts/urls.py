from django.urls import include, path
from accounts.views import UserCreate, LoginView, UserProfileView


urlpatterns = [
    path('register/', UserCreate.as_view()),
    path('login/', LoginView.as_view()),
    path('profile', UserProfileView.as_view({'get': 'list'}))

]
