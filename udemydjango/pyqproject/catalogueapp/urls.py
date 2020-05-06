from django.urls import path
from .views import product_list, product_detail, product_edit, product_delete

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/<int:product_id>/edit/', product_edit, name='product_edit'),
    path('products/<int:product_id>/delete/', product_delete, name='product_delete'),
]
