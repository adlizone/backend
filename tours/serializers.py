"""
Pending:
    Documentation
    Validation
"""

from rest_framework import serializers
from .models import TourPackage, Itinerary, Booking, Destination, Category, Filter

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
    class Meta:
        model = Booking
        fields = '__all__'
