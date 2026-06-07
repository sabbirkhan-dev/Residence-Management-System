from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import Member
from meals.models import Meal
from django.utils import timezone

@login_required
def home(request):

    today = timezone.now().date()

    total_members = Member.objects.filter(
        is_active=True
    ).count()

    breakfast_count = Meal.objects.filter(
        date=today,
        breakfast=True
    ).count()

    dinner_count = Meal.objects.filter(
        date=today,
        dinner=True
    ).count()

    context = {
        "total_members": total_members,
        "breakfast_count": breakfast_count,
        "dinner_count": dinner_count,
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )