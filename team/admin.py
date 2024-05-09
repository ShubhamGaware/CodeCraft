from django.contrib import admin
from team.models import Team

class TeamAdmin(admin.ModelAdmin):
     list_display = ('trainer_photo', 'trainer_name', 'course_name')
     list_display_links = ('trainer_photo',)  # Note: list_display_links should be a tuple
     list_editable = ('trainer_name', 'course_name')  # Note: Corrected field names

admin.site.register(Team,TeamAdmin)
