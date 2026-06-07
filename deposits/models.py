from django.db import models
from members.models import Member


class Deposit(models.Model):

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    date = models.DateField()

    note = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.member} - {self.amount}"