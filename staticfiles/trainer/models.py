from django.db import models

class Trainer(models.Model):
    T_name = models.CharField(max_length=100)
    T_description = models.CharField(max_length=200)
    T_image = models.ImageField(upload_to='Trainer_img/')

    def __str__(self):
        return self.T_name
