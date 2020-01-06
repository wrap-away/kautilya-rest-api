from django.db import models
from django.contrib.auth.models import User

from conference.jitsi import generate_room_name, JITSI_ROOT

class NGO(models.Model):
    """
        Registered NGOs on the Kautilya Platform.
        NGOs are created by Volunteers and can contain 
        any number of volunteers with specific roles.

        @param name str: Name of the NGO
        @param description str: Description for the NGO.
        @param location str: Location of the NGO.
        @attr listings List[VolunteerListing]: Reverse relationships of Listings made by the NGO.
        @attr members List[Volunteer]: Members part of the NGO.
        @attr donations List[Donation]: Donations done to the NGO.
    """
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'<NGO {self.name} {self.location}>'  

class VolunteerListing(models.Model):
    """
        Volunteering listing for an NGO.

        @param created_at datetime.datetime: DateTime on which the listing is created.
        @param title str: Title of the listing.
        @param description str: Description of the listing.
        @attr applications List[VolunteeringApplication]: Reverse relationship of the applications made to the Listing.
        @param ngo NGO: NGO that made the listing.
    """
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    ngo = models.ForeignKey(NGO, related_name='listings', on_delete=models.CASCADE)

    def __str__(self):
        return f'<VolunteerListing {self.created_at} {self.title}>'

    
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
        @attr created_meetings List[Conference]: List of meetings created by the user.
        @attr meetings List[Conference]: Video Conference's volunteer is part of.
        @attr donated List[Donation]: Donations done by Volunteer.
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
        return f'<VolunteeringApplication {self.created_at} {self.listing.title} {self.volunteer.user.username}>'

class Conference(models.Model):
    """ 
        Video Conferencing via meet.jit.si

        @param str meeting_name: automatically generated meet.jit.si room name.
        @param created_by Volunteer: Conference created by volunteer.
        @param members List[Volunteer]: List of members part of the meeting. 
        @param meeting_date datetime.datetime: Date and Time of meeting (in UTC).
        @param title str: Title of the meeting, optional.
        @param description str: description of the meeting.
        @attr str meeting_url: automatically generated meet.jit.si url.
    """
    meeting_name = models.CharField(max_length=60, default=generate_room_name)
    created_by = models.ForeignKey(Volunteer, related_name='created_meetings', on_delete=models.CASCADE)
    members = models.ManyToManyField(Volunteer, related_name='meetings')
    meeting_date = models.DateTimeField()
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    @property
    def meeting_url(self):
        return f'{JITSI_ROOT}{self.meeting_name}'

class Donation(models.Model):
    """ 
        Donate to NGOs.

        @param amount float: Amount donated.
        @param volunteer Volunteer: Donated by Volunteer.
        @param ngo NGO: Donated to NGO.
        @param date datetime.datetime: DateTime of Donation.
    """
    amount = models.FloatField()
    volunteer = models.ForeignKey(Volunteer, related_name='donated', on_delete=models.CASCADE)
    ngo = models.ForeignKey(NGO, related_name='donations', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)