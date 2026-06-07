from django.urls import path
from .views import (
    member_list,
    member_add,
    member_edit,
    member_delete,
)

urlpatterns = [
    path("", member_list, name="member_list"),
    path("add/", member_add, name="member_add"),
    path("edit/<int:pk>/", member_edit, name="member_edit"),
    path("delete/<int:pk>/", member_delete, name="member_delete"),
]