from django.urls import path
from .views import deposit_list, deposit_add

urlpatterns = [
    path("", deposit_list, name="deposit_list"),
    path("add/", deposit_add, name="deposit_add"),
]