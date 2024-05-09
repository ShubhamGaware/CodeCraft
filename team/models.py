from django.db import models

class Team(models.Model):
    trainer_photo = models.FileField(upload_to="team_img/",max_length=250,null=True,default=None)
    trainer_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
