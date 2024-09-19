from django.urls import path, include
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', RegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
]