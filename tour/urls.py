from django.urls import path
from tour import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('package/', views.TourPackageList.as_view()),
    path('package/<int:pk>/', views.TourPackageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)