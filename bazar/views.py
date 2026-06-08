from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Bazar
from .forms import BazarForm


class BazarListView(
    LoginRequiredMixin,
    ListView
):
    model = Bazar
    template_name = "bazar/bazar_list.html"
    context_object_name = "bazars"
    ordering = ["-date"]


class BazarCreateView(
    LoginRequiredMixin,
    CreateView
):
    model = Bazar
    form_class = BazarForm
    template_name = "bazar/bazar_form.html"
    success_url = reverse_lazy("bazar_list")


class BazarUpdateView(
    LoginRequiredMixin,
    UpdateView
):
    model = Bazar
    form_class = BazarForm
    template_name = "bazar/bazar_form.html"
    success_url = reverse_lazy("bazar_list")


class BazarDeleteView(
    LoginRequiredMixin,
    DeleteView
):
    model = Bazar
    template_name = "bazar/bazar_confirm_delete.html"
    success_url = reverse_lazy("bazar_list")