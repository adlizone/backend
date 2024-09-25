from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Order
from .serializers import BookingSerializer, OrderSerializer
from razorpay import Client  # Razorpay integration
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

# Razorpay client setup
client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_SECRET_KEY))

class BookingCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]    
    serializer_class = BookingSerializer

    #Price depends on: price per adult and price per children
    #These fields should be included inside tourpackage later

    def totalPrice(self, adults, children):
        return adults * 10 + children * 10

    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user)
        return booking

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        booking = self.perform_create(serializer)
        
        a = booking.number_of_adults
        b = booking.number_of_children

        total_amount = self.totalPrice(a,b)

        # Create Razorpay Order
        razorpay_order = client.order.create({
            'amount': int(total_amount * 100),  # Amount in paise
            'currency': 'INR',
            'payment_capture': '1'
        })
        
        # Create Order in DB
        Order.objects.create(
            booking=booking,
            razorpay_order_id=razorpay_order['id'],
            amount=total_amount,
            status='created'
        )

        return Response({
            'booking_id': booking.id,
            'order_id': razorpay_order['id'],
            'amount': razorpay_order['amount'],
            'currency': razorpay_order['currency']
        }, status=status.HTTP_201_CREATED)        
        


class PaymentSuccessView(generics.UpdateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        razorpay_order_id = request.data.get('razorpay_order_id')
        payment_status = request.data.get('status')

        try:
            order = Order.objects.get(razorpay_order_id=razorpay_order_id)
            if payment_status == 'success':
                order.status = 'success'
                order.save()

                # Update the booking status
                order.booking.status = 'paid'
                order.booking.save()

            return Response({'status': 'success'}, status=status.HTTP_200_OK)

        except Order.DoesNotExist:
            return Response({'error': 'Invalid order ID'}, status=status.HTTP_400_BAD_REQUEST)