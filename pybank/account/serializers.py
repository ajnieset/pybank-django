from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "url",
            "balance",
            "routing_number",
            "account_type",
            "user",
            "created",
            "updated",
        ]
        read_only_fields = ["created", "updated"]
