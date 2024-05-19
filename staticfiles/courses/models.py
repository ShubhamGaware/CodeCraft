from django.db import models

class Course(models.Model):
    course_icon = models.FileField(upload_to="cource/",max_length=250,null=True,default=None)
    course_name = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    current_batch_date = models.DateField()
    batch_timing = models.CharField(max_length=100)
    upcoming_batch = models.DateField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
