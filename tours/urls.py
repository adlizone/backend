from django.urls import path, re_path
from tours import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.TourPackageList.as_view(), name='tour-list'),
    path('<int:tour_id>/',views.TourPackageInstance.as_view(), name='tour-instance'),
    path('<int:tour_id>/itineraries/', views.ItineraryList.as_view(), name='itinerary-list'),
    path('<int:tour_id>/categories/', views.CategoryList.as_view(), name='category-list'),
    path('<int:tour_id>/destinations/', views.DestinationList.as_view(), name='destination-list'),
    path('<int:tour_id>/filters/', views.FilterList.as_view(), name="filter-list"),
    path('bookings/', views.BookingCreate.as_view(), name='bookings'),
    path('categories/', views.CategoriesAll.as_view(), name='categories-all'),
    path('search/<int:category_id>/', views.TourSearch.as_view(), name='tour-search'),
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html"),name="all-urls"),
]

urlpatterns = format_suffix_patterns(urlpatterns)