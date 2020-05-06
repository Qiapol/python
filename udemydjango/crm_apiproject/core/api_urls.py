from django.urls import path, include

from .api_views import customer_list, customer_and_log, search_customer, filter_logs, register_customer, \
                       register_customer_and_log

urlpatterns = [
    path("customer/", customer_list, name="customer_list"),
    path('customer/<int:customer_id>/logs', customer_and_log, name='customer_and_log'),
    path('customer/search', search_customer, name='search_customer'),
    path('customer/filter_logs', filter_logs, name='filter_logs'),
    path('customer/register', register_customer, name='register_customer'),
    path('customer/register_and_log', register_customer_and_log, name='register_customer_and_log'),
]
