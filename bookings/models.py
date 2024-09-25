from django.db import models
from django.conf import settings
from tours.models import TourPackage

from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    DecimalValidator,
)

from util.model_validators import (
        arrival_date_validator,
        phone_number_validator,
        name_validator_list,
        #min_words_validator,
    )

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)

    msg = "Enter a value in the range 1-30"
    number_of_adults = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1,msg),MaxValueValidator(30,msg)],
    )

    msg = "Enter a value in the range 0-30"
    number_of_children = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0,msg),MaxValueValidator(30,msg)],
    )
    
    arrival_date = models.DateField(
        blank=True,
        null=True,
        validators = [arrival_date_validator],
        auto_now=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')  # pending, paid, etc.

class Order(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='order')
    razorpay_order_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='created')  # created, success, failed
    created_at = models.DateTimeField(auto_now_add=True)
