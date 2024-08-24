"""
Pending:
    Documentation
"""

from rest_framework import serializers
from .models import TourPackage, Itinerary, Booking, Destination, Category, Filter
from util.validators import ( 
        phone_number_validator, 
        person_count_validator,
        arrival_date_validator,
    )
from django.core.validators import (
        MinValueValidator,
        MaxValueValidator,
    )

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        exclude = ['created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        exclude = ['created_at', 'updated_at']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        exclude = ['created_at', 'updated_at']

class TourPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TourPackage
        exclude = ['categories', 'filters', 'destinations',
            'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    message_adult = "Enter a value in the range 1-30"
    message_child = "Enter a value in the range 0-30"

    customer_phone = serializers.CharField(
        validators=[phone_number_validator]
    )
    adults = serializers.IntegerField(
        validators=[MinValueValidator(1,message_adult),MaxValueValidator(30,message_adult)]
    )
    children = serializers.IntegerField(
        validators=[MinValueValidator(0,message_child),MaxValueValidator(30,message_child)]
    )
    arrival_date = serializers.DateTimeField(
        validators=[arrival_date_validator]
    )
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 
            'adults', 'children', 'arrival_date', 'tour_package',
            'booking_date']
       