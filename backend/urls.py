from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tours/', include('tours.urls')),
    path('api/users/', include('users.urls')),
    path('api/bookings/', include('bookings.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html"),name="all-urls"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	