"""kautilya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from api.views import (
    VolunteerViewSet, 
    VolunteerListingViewSet, 
    VolunteeringApplicationViewSet,
    NGOViewSet,
    ConferenceViewSet,
    DonationViewSet,
)

router = routers.SimpleRouter()
router.register(r'volunteer', VolunteerViewSet)
router.register(r'ngo', NGOViewSet)
router.register(r'listing', VolunteerListingViewSet)
router.register(r'application', VolunteeringApplicationViewSet)
router.register(r'conference', ConferenceViewSet)
router.register(r'donation', DonationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include(router.urls)),
]
