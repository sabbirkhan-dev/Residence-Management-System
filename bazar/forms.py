from django import forms
from .models import Bazar


class BazarForm(forms.ModelForm):

    class Meta:
        model = Bazar
        fields = [
            "date",
            "amount",
            "details",
        ]

        widgets = {
            "date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter amount"
                }
            ),
            "details": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter details"
                }
            ),
        }