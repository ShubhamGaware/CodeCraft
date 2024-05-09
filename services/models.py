from django.db import models

class Services(models.Model):
    service_icon = models.FileField(upload_to="services_img/",max_length=250,null=True,default=None)
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=100)
