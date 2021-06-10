from django.urls import path
from .views import add, add_save


urlpatterns = [
    path('add/', add, name='add'),
    path('add_save/', add_save, name = 'add_save')
]
