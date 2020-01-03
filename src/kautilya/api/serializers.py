from rest_framework import serializers
from api.models import Volunteer, VolunteerListing, VolunteeringApplication, NGO
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class VolunteerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Volunteer
        fields = [  
            'user',
            'id',
            'role_type'
        ]
        extra_kwargs = {
            'id' : {
                'read_only': True
            },
            'role_type': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['user']['email'],
            username=validated_data['user']['username'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name']
        )
        user.set_password(validated_data['user']['password'])
        user.save()

        volunteer = Volunteer(user=user)
        volunteer.save()
        return volunteer

class VolunteeringApplicationSerializer(serializers.ModelSerializer):
    volunteer = serializers.PrimaryKeyRelatedField(queryset=Volunteer.objects.all())
    listing = serializers.PrimaryKeyRelatedField(queryset=VolunteerListing.objects.all())
    
    class Meta:
        model = VolunteeringApplication
        fields = [
            'id',
            'listing',
            'volunteer'
        ]

        extra_kwargs = {
            'id' : {
                'read_only': True
            }
        }
        
class VolunteerListingSerializer(serializers.ModelSerializer):
    applications = VolunteeringApplicationSerializer(read_only=True, many=True)
    ngo = serializers.PrimaryKeyRelatedField(queryset=NGO.objects.all(), many=True)

    class Meta:
        model = VolunteerListing
        fields = [
            'id',
            'title',
            'description',
            'ngo',
            'applications'
        ]

        extra_kwargs = {
            'id' : {
                'read_only': True
            },
            'applications': {
                'read_only': True
            }
        }
        
    def create(self, validated_data):
        """ 
            Create new VolunteerListing,
            Convert NGO id to NGO Instance,
            Add VolunteerListing to NGO Instance,
            Return VolunteerListing
        """
        ngo = validated_data.pop('ngo')[0]
        
        new_listing = VolunteerListing(**validated_data)
        new_listing.save()

        ngo.listings.add(new_listing)
        ngo.save()

        return new_listing

class VolunteeringApplicationForNGOSerializer(VolunteeringApplicationSerializer):
    class Meta(VolunteeringApplicationSerializer.Meta):
        fields = [
            'id',
            'volunteer'
        ]

class VolunteerListingForNGOSerializer(VolunteerListingSerializer):
    applications = VolunteeringApplicationForNGOSerializer(read_only=True, many=True)
    
    class Meta(VolunteerListingSerializer.Meta):
        fields = [
            'id',
            'title',
            'description',
            'applications'
        ]

class NGOSerializer(serializers.ModelSerializer):
    listings  = VolunteerListingForNGOSerializer(read_only=True, many=True)

    class Meta:
        model = NGO
        fields = [
            'id',
            'name',
            'description',
            'location',
            'listings'
        ]
        etra_kwargs = {
            'id' : {
                'read_only': True
            },
            'listings': {
                'read_only': True
            }
        }