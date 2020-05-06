from django.contrib import admin
from django.urls import path, include

from .views import news_list, news_detail, item_list, item_detail

urlpatterns = [
    path('news/', news_list, name='news_list_api'),
    path('news/<int:news_id>', news_detail, name='news_detail_api'),
    path('items/', item_list, name='item_list_api'),
    path('items/<int:item_id>', item_detail, name='item_detail_api'),
]
