from django.urls import path, include
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register("books", views.BooksView)
router.register("categories", views.CategoriesView)
router.register("author", views.AuthorView)

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls))
]