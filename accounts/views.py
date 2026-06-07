from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView
# Create your views here.

# RegisterView
class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


# UserLoginView
class UserLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        return "/"