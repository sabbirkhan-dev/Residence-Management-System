from django.shortcuts import render, redirect
from .models import Deposit
from .forms import DepositForm


def deposit_list(request):

    deposits = Deposit.objects.all().order_by("-date")

    return render(
        request,
        "deposits/list.html",
        {
            "deposits": deposits
        }
    )


def deposit_add(request):

    if request.method == "POST":

        form = DepositForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("deposit_list")

    else:
        form = DepositForm()

    return render(
        request,
        "deposits/add.html",
        {
            "form": form
        }
    )