from django.urls import path
from . import views

urlpatterns = [
    path('', views.bazar_list, name='bazar_list'),
]