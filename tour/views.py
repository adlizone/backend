from .serializers import TourPackageSerializer
from .models import TourPackage	
from rest_framework import generics

class TourPackageList(generics.ListCreateAPIView):
    """
    List all packages, or create a new package.
    """

    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer

class TourPackageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a package instance.
    """
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
