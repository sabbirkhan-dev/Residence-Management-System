from django import forms
from django.utils import timezone
from .models import Deposit


class DepositForm(forms.ModelForm):

    date = forms.DateField(
        initial=timezone.now().date,
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Deposit
        fields = [
            "member",
            "amount",
            "date",
            "note",
        ]