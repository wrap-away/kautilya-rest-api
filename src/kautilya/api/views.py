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
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return super().get_permissions()
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #         return [permission() for permission in permission_classes]
    
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class NGOViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle NGO CRUD.
    """
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return super().get_permissions()
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #         return [permission() for permission in permission_classes]

    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

class VolunteeringApplicationViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle VolunteeringApplications.
    """
    # def get_permissions(self):
    #     permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = VolunteeringApplication.objects.all()
    serializer_class = VolunteeringApplicationSerializer

class VolunteerListingViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle VolunteerListing CRUD.
    """
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return super().get_permissions()
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #         return [permission() for permission in permission_classes]

    queryset = VolunteerListing.objects.all()
    serializer_class = VolunteerListingSerializer

class ConferenceViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle Conferences.
    """
    # def get_permissions(self):
    #     permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class DonationViewSet(viewsets.ModelViewSet):
    """
        ViewSet to handle Donation to NGOs.
    """
    # def get_permissions(self):
    #     permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    queryset = Donation.objects.all()
    serializer_class = DonationSerializer