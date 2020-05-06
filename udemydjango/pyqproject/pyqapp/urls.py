from django.urls import path
from .views import index, good


urlpatterns = [
    path('good', good, name='good'),
    path('', index, name='index'),
]
