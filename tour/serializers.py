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
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = '__all__'

class TourPackageSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    filters = FilterSerializer(many=True, read_only=True)
    itineraries = ItinerarySerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
