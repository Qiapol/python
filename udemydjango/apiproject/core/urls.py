from django.contrib import admin
from django.urls import path, include

from .views import index, news_detail, item_detail

urlpatterns = [
    path('', index, name='index'),
    path('news/<int:news_id>', news_detail, name='news_detail'),
    path('item/<int:item_id>', item_detail, name='item_detail'),

]