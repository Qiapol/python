from django.urls import path
from .views import hellofunction

# as_view()はclass_based_viewの時には必ず使用する必要がある(詳細な動きは不明)
urlpatterns = [
    path('world/', hellofunction),
]
