from django.contrib import admin
from .models import Vegetable, Comment, Good

# Register your models here.

admin.site.register(Vegetable)
admin.site.register(Comment)
admin.site.register(Good)
