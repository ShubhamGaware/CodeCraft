from django.contrib import admin
from gallery.models import class_Photo

@admin.register(class_Photo)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'image',)

