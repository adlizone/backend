"""
Pending:
    Documentation
        ..add docstrings to each model
"""	

from django.db import models
from django.core.validators import ( MaxValueValidator,
    MinValueValidator, MaxLengthValidator, MinLengthValidator,
    DecimalValidator )

from util.model_validators import (
        arrival_date_validator,
        phone_number_validator,
        name_validator_list,
        #min_words_validator,
    )

class Destination(models.Model):
    name = models.CharField(
        max_length=255,
        validators=name_validator_list,
    )
    description = models.TextField(
        blank=True, 
        validators=[MaxLengthValidator(300, "Too long description")]
    )
    image = models.ImageField(upload_to='destination_images/', null=True,blank=True)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        validators=name_validator_list
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Filter(models.Model):
    name = models.CharField(
        max_length=255,
        validators=name_validator_list,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=name_validator_list
    )
    description = models.TextField(
        blank=True,
        null=True,
        validators=[MaxLengthValidator(500, "Too long description")],
    )
    duration = models.IntegerField(
        help_text="Duration in days",
        blank=True,
        null=True,
        validators=[MaxValueValidator(30,"Range is 1-30"), MinValueValidator(1,"Range is 1-30")]
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True,
        null=True,
        validators=[DecimalValidator(10,2)],
    )
    availability = models.BooleanField(default=True,blank=True)
    destinations = models.ManyToManyField(Destination,blank=True)
    categories = models.ManyToManyField(Category,blank=True)
    filters = models.ManyToManyField(Filter,blank=True)
    image = models.ImageField(upload_to='tour_images/', null=True,blank=True)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    title = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(2,"Title can not be shorter than two letters")],
    )
    description = models.TextField(
        validators=[MaxLengthValidator(1000, "Too long description")]
    )
    day_number = models.IntegerField(
        validators=[MaxValueValidator(30,"Range is 1-30"), MinValueValidator(1,"Range is 1-30")]
    )
    tour_package = models.ForeignKey(TourPackage, related_name='itineraries', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - Day {self.day_number}"

class Booking(models.Model):
    message_adult = "Enter a value in the range 1-30"
    message_child = "Enter a value in the range 0-30"

    customer_name = models.CharField(
        max_length=255,
        validators=name_validator_list,
    )
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(
        max_length=10,
        validators = [phone_number_validator],
    )
    adults = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1,message_adult),MaxValueValidator(30,message_adult)],
    )
    children = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0,message_child),MaxValueValidator(30,message_child)],
    )
    arrival_date = models.DateTimeField(
        blank=True,
        null=True,
        validators = [arrival_date_validator],
        auto_now=True,
    )
    tour_package = models.ForeignKey(TourPackage, related_name='bookings', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.tour_package.name}"
