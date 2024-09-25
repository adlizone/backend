"""
Pending:
    Documentation
"""

from rest_framework import serializers
from .models import TourPackage, Itinerary, Destination, Category, Filter
from util.api_validators import ( 
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