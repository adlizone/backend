from .serializers import ( TourPackageSerializer, ItinerarySerializer,
    CategorySerializer, DestinationSerializer, FilterSerializer)

from .models import (TourPackage, Itinerary, Category, 
    Destination, Filter)
	
from rest_framework import generics

class TourPackageList(generics.ListAPIView):
    """
    List all packages.
    """

    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

class TourPackageInstance(generics.RetrieveAPIView):
    """
    Return a single tour package instance.
    """
    lookup_url_kwarg = "tour_id"
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

class ItineraryList(generics.ListAPIView):
    """
    List all itineraries for a given instance.
    """
    serializer_class = ItinerarySerializer

    def get_queryset(self):
        tour_id = self.kwargs["tour_id"]
        return Itinerary.objects.filter(tour_package=tour_id)

class CategoryList(generics.ListAPIView):
    """
    List all categories for a given instance.
    """
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        tour_id = self.kwargs["tour_id"]
        return TourPackage.objects.get(id=tour_id).categories

class DestinationList(generics.ListAPIView):
    """
    List all destinations for a given instance.
    """
    serializer_class = DestinationSerializer
    
    def get_queryset(self):
        tour_id = self.kwargs["tour_id"]
        return TourPackage.objects.get(id=tour_id).destinations

class FilterList(generics.ListAPIView):
    """
    List all filters for a given instance.
    """
    serializer_class = FilterSerializer
    
    def get_queryset(self):
        tour_id = self.kwargs["tour_id"]
        return TourPackage.objects.get(id=tour_id).filters

class TourSearch(generics.ListAPIView):
    """
    List all tour packages for a given category.
    """
    serializer_class = TourPackageSerializer

    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return Category.objects.get(id=category_id).tourpackage_set.all()

class CategoriesAll(generics.ListAPIView):
    """
    List all available categories.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()