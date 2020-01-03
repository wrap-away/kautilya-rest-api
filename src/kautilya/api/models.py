from django.db import models
from django.contrib.auth.models import User

class VolunteerListing(models.Model):
    """
        Volunteering listing for an NGO.

        @param created_at datetime.datetime: DateTime on which the listing is created.
        @param title str: Title of the listing.
        @param description str: Description of the listing.
        @attr applications List[VolunteeringApplication]: Reverse relationship of the applications made to the Listing.
        @attr ngo NGO: Reverse relationship of the NGO that made the listing.
    """
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'<VolunteerListing {self.created_at} {self.title}>'

class NGO(models.Model):
    """
        Registered NGOs on the Kautilya Platform.
        NGOs are created by Volunteers and can contain 
        any number of volunteers with specific roles.

        @param name str: Name of the NGO
        @param description str: Description for the NGO.
        @param location str: Location of the NGO.
        @param listings List[VolunteerListing]: Listings made by the NGO.
        @attr members List[Volunteer]: Members part of the NGO.
    """
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    listings = models.ManyToManyField(VolunteerListing, related_name='ngo')

    def __str__(self):
        return f'<NGO {self.name} {self.location}>'  
    
class Volunteer(models.Model):
    """
        Registered Volunteers on the Kautilya Platform,
        Could be verified or unverified volunteers,
        _User_ of the platform.

        @param user django.contrib.auth.models: Reference to the django User model.
        @param role_type str: Role Type as a member of the platform or any organization. 
                                           Use for ACL inside NGO Dashboard, bad but saves time, 
                                           replace with Users/Groups.
        @param ngo List[NGO]: List of NGOs user is a member of.
        @attr applications List[VolunteeringApplication]: Reverse relationship of applications for volunteering made by the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_type =  models.CharField(max_length=100, default='Member')
    ngo = models.ManyToManyField(NGO, related_name='members')

    def __str__(self):
        return f'<Volunteer {self.user.username} {self.role_type}>'

class VolunteeringApplication(models.Model):
    """
        Application for a VolunteerListing

        @param created_at datetime.datetime: DateTime on which application is created.
        @param listing VolunteeringListing: Listing the application is a part of.
        @param volunteer Volunteer: relationship of the volunteer that made the application.
    """
    created_at = models.DateTimeField(auto_now=True)
    listing = models.ForeignKey(VolunteerListing, related_name='applications', on_delete=models.CASCADE)
    volunteer = models.ForeignKey(Volunteer, related_name='applications', on_delete=models.CASCADE)

    def __str__(self):
        return f'<VolunteeringApplication {self.created_at} {self.listing.title} {self.volunteer.user.usenrame}>'