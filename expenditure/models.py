from django.conf import settings
from django.db import models

from budget.models import Category


class Expenditure(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="지출일")
    amount = models.DecimalField(max_digits=10, verbose_name="지출 금액", decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    memo = models.TextField(blank=True, null=True)
    excluded_total = models.BooleanField(default=False)
