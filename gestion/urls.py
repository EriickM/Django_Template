from django.urls import path
from .views import index, show

urlpatterns = [
    path('', index),
    path('details/<int:pk>', show),
]