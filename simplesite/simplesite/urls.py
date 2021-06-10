from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('bboard/', include('bboard.urls')),
    path('admin/', admin.site.urls),
    path('stady/', include('stady.urls')),
]
