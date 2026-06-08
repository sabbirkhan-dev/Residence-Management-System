from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum

from members.models import Member
from meals.models import Meal
from deposits.models import Deposit
from bazar.models import Bazar


@login_required
def home(request):

    today = timezone.now().date()

    month = today.month
    year = today.year

    # Active Members
    total_members = Member.objects.filter(
        is_active=True
    ).count()

    # Today's Breakfast
    breakfast_count = Meal.objects.filter(
        date=today
    ).aggregate(
        total=Sum("breakfast")
    )["total"] or 0

    # Today's Dinner
    dinner_count = Meal.objects.filter(
        date=today
    ).aggregate(
        total=Sum("dinner")
    )["total"] or 0

    # Today's Total Meal
    today_total_meal = (
        breakfast_count +
        dinner_count
    )

    # Today's Bazar Cost
    today_bazar_cost = Bazar.objects.filter(
        date=today
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # Monthly Breakfast
    monthly_breakfast = Meal.objects.filter(
        date__month=month,
        date__year=year
    ).aggregate(
        total=Sum("breakfast")
    )["total"] or 0

    # Monthly Dinner
    monthly_dinner = Meal.objects.filter(
        date__month=month,
        date__year=year
    ).aggregate(
        total=Sum("dinner")
    )["total"] or 0

    # Monthly Total Meal
    monthly_meal = (
        monthly_breakfast +
        monthly_dinner
    )

    # Monthly Deposit
    monthly_deposit = Deposit.objects.filter(
        date__month=month,
        date__year=year
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # Monthly Bazar
    monthly_bazar = Bazar.objects.filter(
        date__month=month,
        date__year=year
    ).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # Meal Rate
    meal_rate = 0

    if monthly_meal > 0:
        meal_rate = round(
            float(monthly_bazar / monthly_meal),
            2
        )

    # Balance
    balance = round(
        float(monthly_deposit - monthly_bazar),
        2
    )

    context = {
        "today": today,

        "total_members": total_members,

        "breakfast_count": breakfast_count,
        "dinner_count": dinner_count,
        "today_total_meal": today_total_meal,

        "today_bazar_cost": today_bazar_cost,

        "monthly_deposit": monthly_deposit,
        "monthly_bazar": monthly_bazar,
        "monthly_meal": monthly_meal,

        "meal_rate": meal_rate,
        "balance": balance,
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )