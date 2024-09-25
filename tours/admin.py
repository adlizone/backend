from django.contrib import admin
from .models import ( TourPackage, Destination, Category,
                      Filter, Itinerary)

admin.site.register(TourPackage)
admin.site.register(Destination)
admin.site.register(Category)
admin.site.register(Filter)
admin.site.register(Itinerary)

