from django.urls import path
from .views import BookingCreateView, PaymentSuccessView

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='create-booking'),
    path('payment-success/', PaymentSuccessView.as_view(), name='payment-success'),
]
