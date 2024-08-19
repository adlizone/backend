from django.urls import path
from tours import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.TourPackageList.as_view(), name='tour-list'),
    path('<int:tour_id>/itineraries', views.ItineraryList.as_view(), name='itinerary-list'),
    path('<int:tour_id>/categories', views.CategoryList.as_view(), name='category-list'),
    path('<int:tour_id>/destinations', views.DestinationList.as_view(), name='destination-list'),
    path('<int:tour_id>/filters', views.FilterList.as_view(), name="filter-list"),
    path('bookings/', views.BookingCreate.as_view(), name='bookings'),
    #path('search/', TourSearch.as_view(), name='tour-search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)