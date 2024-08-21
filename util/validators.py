from rest_framework import serializers
import re

def phone_number_validator(value):
    # Regex pattern to allow only 10 digits, no leading '+', no spaces or dashes
    phone_regex = re.compile(r'^\d{10}$')
    if not phone_regex.match(value):
        raise serializers.ValidationError("Phone number must be exactly 10 digits.")
    return value

def person_count_validator(value):
    if value < 1 or value > 30:
        raise serializers.ValidationError("Please enter a value in the range 1-30")
    return value