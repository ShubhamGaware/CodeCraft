from django.contrib import admin
from contact_form.models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at','message')
    search_fields = ('name', 'email', 'phone', 'created_at','message')
    list_filter = ('created_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)
