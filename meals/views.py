from django.shortcuts import render, redirect
from .models import Meal
from .forms import MealForm


def meal_list(request):
    meals = Meal.objects.all().order_by("-date")

    return render(
        request,
        "meals/list.html",
        {
            "meals": meals
        }
    )


def meal_add(request):

    if request.method == "POST":

        form = MealForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("meal_list")

    else:
        form = MealForm()

    return render(
        request,
        "meals/add_meal.html",
        {
            "form": form
        }
    )