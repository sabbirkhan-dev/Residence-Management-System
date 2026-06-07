from django import forms
from django.utils import timezone
from .models import Meal


class MealForm(forms.ModelForm):

    date = forms.DateField(
        initial=timezone.now().date,
        widget=forms.DateInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Meal

        fields = [
            "member",
            "date",
            "breakfast",
            "dinner",
        ]