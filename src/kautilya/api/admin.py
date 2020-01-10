from django.contrib import admin

from api.models import (NGO, VolunteerListing, VolunteeringApplication, 
                        Volunteer, Conference, Donation)

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location')


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'role_type')

@admin.register(VolunteerListing)
class VolunteerListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'ngo', 'created_at')


@admin.register(VolunteeringApplication)
class VolunteeringApplicationAdmin(admin.ModelAdmin):
    list_display = ('listing', 'volunteer', 'created_at')


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('meeting_name', 'title', 'created_by', 'meeting_date')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('ngo', 'volunteer', 'status', 'amount', 'date')