from rest_framework import serializers
from .models import Booking, Order

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['tour_package', 'number_of_adults', 'number_of_children', 'arrival_date']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['razorpay_order_id', 'amount', 'status']
