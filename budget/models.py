from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="카테고리 명")

    def __str__(self):
        return self.name


class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="금액")
    period = models.DateTimeField(verbose_name="기간")

    def __str__(self):
        return f"{self.category} - {self.amount}"
