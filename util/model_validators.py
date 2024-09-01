from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
import re
from datetime import datetime

name_validator_list = [
        MaxLengthValidator(100, 'Name can not be longer than 100 letters'),
        MinLengthValidator(2, 'Name can be shorter then two letters'),
        RegexValidator (
            regex = '^[A-Za-z\s]+$',
            message='Name must contain only letters and spaces',
            code='invalid_name'
        )
    ]

def min_words_validator(min_words=20, custom_message=None):
    def validator(value):
        words = value.split()
        if len(words) < min_words:
            message = custom_message or f'The description must be at least {min_words} words long.'
            raise ValidationError(message)
    return validator

def phone_number_validator(value):
    # Regex pattern to allow only 10 digits, no leading '+', no spaces or dashes
    phone_regex = re.compile(r'^\d{10}$')
    if not phone_regex.match(value):
        raise ValidationError("Phone number must be exactly 10 digits.")
    return value

def person_count_validator(value):
    if value < 1 or value > 30:
        raise ValidationError("Please enter a value in the range 1-30")
    return value

def arrival_date_validator(value):
    if value < datetime.now():
        raise ValidationError("Arrival date cannot be in the past.")
    return value