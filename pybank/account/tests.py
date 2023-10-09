from django.contrib.auth.models import User
from django.test import TestCase

from pybank.account.models import Account


class AccountTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user", email="user@test.com")
        Account.objects.create(
            balance=0.00, routing_number=12345123, account_type="checking", user=user
        )

    def test_get_account(self):
        account = Account.objects.get(pk=1)
        self.assertEqual(account.balance, 0.00)
        self.assertEqual(account.user.username, "test_user")

    def test_update_account(self):
        account = Account.objects.get(pk=1)
        self.assertEqual(account.balance, 0.00)

        account.balance = 12.53
        account.save()

        updated_account = Account.objects.get(pk=1)
        self.assertEqual(updated_account.balance, 12.53)
