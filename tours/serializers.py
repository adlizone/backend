"""
Pending:
    Documentation
    Validation
"""

from rest_framework import serializers
from .models import TourPackage, Itinerary, Booking, Destination, Category, Filter
from util.validators import phone_number_validator, person_count_validator

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
    customer_phone = serializers.CharField(validators=[phone_number_validator])
    adults = serializers.IntegerField(validators=[person_count_validator])
    children = serializers.IntegerField(validators=[person_count_validator])
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 
            'adults', 'children', 'arrival_date', 'tour_package',
            'booking_date']