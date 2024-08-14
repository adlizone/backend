"""
Pending:
    Documentation
    Validation
"""

from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Filter(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    destinations = models.ManyToManyField(Destination)
    categories = models.ManyToManyField(Category)
    filters = models.ManyToManyField(Filter)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    day_number = models.IntegerField()
    tour_package = models.ForeignKey(TourPackage, related_name='itineraries', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - Day {self.day_number}"

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    tour_package = models.ForeignKey(TourPackage, related_name='bookings', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.tour_package.name}"
