import django.contrib
from django.urls import path, include


urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', django.contrib.admin.site.urls),
]
