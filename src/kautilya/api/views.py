from django.shortcuts import render

from rest_framework import (
    views, 
    parsers, 
    renderers, 
    viewsets,
    status,
    permissions
)
from rest_framework.response import Response

from api.serializers import (
    VolunteerSerializer, 
    VolunteerListingSerializer, 
    VolunteeringApplicationSerializer, 
    NGOSerializer,
    ConferenceSerializer,
    DonationSerializer
)

from api.models import (
    Volunteer, 
    VolunteerListing, 
    VolunteeringApplication, 
    NGO, 
    Conference,
    Donation
)

from oauth2_provider.contrib.rest_framework import (
    TokenHasReadWriteScope, 
    TokenHasScope
)

class VolunteerViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle Volunteer CRUD.
    """
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class NGOViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle NGO CRUD.
    """
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

class VolunteeringApplicationViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle VolunteeringApplications.
    """
    queryset = VolunteeringApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer

class VolunteerListingViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle VolunteerListing CRUD.
    """
    queryset = VolunteerListing.objects.all()
    serializer_class = VolunteerListingSerializer

class ConferenceViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle Conferences.
    """
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class DonationViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle Donation to NGOs.
    """
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer