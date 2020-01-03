from django.shortcuts import render

from rest_framework import views, parsers, renderers, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from api.serializers import VolunteerSerializer, VolunteerListingSerializer, VolunteeringApplicationSerializer, NGOSerializer
from api.models import Volunteer, VolunteerListing, VolunteeringApplication, NGO

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

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