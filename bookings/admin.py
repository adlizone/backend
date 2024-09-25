from django.contrib import admin
from .models import Booking, Order

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour_package', 'number_of_adults', 'number_of_children', 'arrival_date', 'status')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('booking', 'razorpay_order_id', 'amount', 'status', 'created_at')
