from django.core.exceptions import ValidationError


def validate_alphabetic(value):
    if not value.isalpha():
        raise ValidationError("Value should be all alphabetical symbols.")
