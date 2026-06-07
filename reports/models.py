from django.db import models

# Create your models here.
class MessMonth(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.month}-{self.year}"