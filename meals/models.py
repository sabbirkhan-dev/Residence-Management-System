from django.db import models
from members.models import Member


BREAKFAST_CHOICES = [
    (0, "0"),
    (0.5, "0.5"),
    (1, "1"),
    (1.5, "1.5"),
    (2, "2"),
    (2.5, "2.5"),
    (3, "3"),
]

DINNER_CHOICES = [
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
]


class Meal(models.Model):

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    breakfast = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.5,
        choices=BREAKFAST_CHOICES
    )

    dinner = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1,
        choices=DINNER_CHOICES
    )

    def total_meal(self):
        return self.breakfast + self.dinner

    def __str__(self):
        return f"{self.member} - {self.date}"