from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    balance = models.FloatField()
    routing_number = models.PositiveIntegerField()
    account_type = models.CharField(max_length=16)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
