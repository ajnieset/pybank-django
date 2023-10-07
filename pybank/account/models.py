from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


ACCOUNT_TYPES = [
    (1, "savings"),
    (2,"checking")
]

class Account(models.Model):
    balance = models.FloatField()
    routing_number = models.PositiveIntegerField()
    account_type = models.CharField(choices=ACCOUNT_TYPES, max_length=30)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
