from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def account_type_validator(value: str):
    if value not in ["checking", "savings"]:
        raise ValidationError(
            _("%(value)s is not a valid account type"),
            params={"value": value},
        )
