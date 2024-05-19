from django.contrib import admin
from services.models import Services

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_name', 'service_description')
    list_display_links = ('service_icon',)  # Note: list_display_links should be a tuple
    list_editable = ('service_name', 'service_description')  # Note: Corrected field names

admin.site.register(Services, ServiceAdmin)

