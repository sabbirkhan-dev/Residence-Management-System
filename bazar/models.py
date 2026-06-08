from django.db import models

# Create your models here.

class Bazar(models.Model):

    date = models.DateField()

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    details = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.date} - {self.amount}"