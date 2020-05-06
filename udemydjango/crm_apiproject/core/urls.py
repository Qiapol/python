from django.urls import path

from .views import index, customer_detail

app_name = "core"
urlpatterns = [
    path("", index, name="index"),
    path("customer/<int:customer_id>", customer_detail, name="customer_detail"),
]
