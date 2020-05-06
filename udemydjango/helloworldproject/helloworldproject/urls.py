from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloWorldView

# as_view()はclass_based_viewの時には必ず使用する必要がある(詳細な動きは不明)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworldapp.urls'))
]
