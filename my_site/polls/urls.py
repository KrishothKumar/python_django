from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add, name='adds'),
    path('', views.index, name='index'),
]
