from django.urls import path, include

from .views import cart_add, cart_list, cart_delete

urlpatterns = [
    path('cart/<int:product_id>/add/', cart_add, name='cart_add'),
    path('cart/', cart_list, name='cart_list'),
    path('cart/<int:product_id>/delete/', cart_delete, name='cart_delete'),
]
