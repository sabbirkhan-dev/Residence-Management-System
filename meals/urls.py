from django.urls import path
from .views import meal_list, meal_add

urlpatterns = [
    path("", meal_list, name="meal_list"),
    path("add/", meal_add, name="meal_add"),
]