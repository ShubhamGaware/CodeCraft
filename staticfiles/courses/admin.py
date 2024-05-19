from django.contrib import admin
from django.contrib import admin
from courses.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_icon', 'course_name', 'professor_name', 'current_batch_date', 'batch_timing',
                    'upcoming_batch', 'fees')
    list_display_links = ('course_icon',)
    list_editable =('course_name', 'professor_name', 'current_batch_date', 'batch_timing',
                    'upcoming_batch', 'fees')
admin.site.register(Course, CourseAdmin)

# Register your models here.
