
from django.urls import path

from .import views

urlpatterns = [
    path("url/", views.index),
    path('func/',views.function),
]