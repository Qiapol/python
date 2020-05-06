from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pyqapp/', include('pyqapp.urls')),
    path('catalogueapp/', include('catalogueapp.urls')),
    path('cartapp/', include('cartapp.urls')),
]
