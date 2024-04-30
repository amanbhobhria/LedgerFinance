

from django.core.exceptions import ValidationError


class DjangoLedgerConfigurationError(Exception):
    pass


class InvalidDateInputError(ValidationError):
    pass


class InvalidRoleError(ValidationError):
    pass


class TransactionNotInBalanceError(ValidationError):
    pass
