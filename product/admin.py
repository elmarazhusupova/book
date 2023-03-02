from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Feedback)
admin.site.register(Cart)
