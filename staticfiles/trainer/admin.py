from django.contrib import admin
from trainer.models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('T_image','T_name', 'T_description',)
    list_display_links = ('T_image',)  # Note: list_display_links should be a tuple
    list_editable = ('T_name', 'T_description')  
