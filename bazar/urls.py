from django.urls import path
from .views import (
    BazarListView,
    BazarCreateView,
    BazarUpdateView,
    BazarDeleteView,
)

urlpatterns = [

    path(
        "",
        BazarListView.as_view(),
        name="bazar_list"
    ),

    path(
        "add/",
        BazarCreateView.as_view(),
        name="bazar_add"
    ),

    path(
        "<int:pk>/edit/",
        BazarUpdateView.as_view(),
        name="bazar_edit"
    ),

    path(
        "<int:pk>/delete/",
        BazarDeleteView.as_view(),
        name="bazar_delete"
    ),

]