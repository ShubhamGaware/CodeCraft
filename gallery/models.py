from django.db import models

class class_Photo(models.Model):
    label_choices = [
        ('Campus Drive', 'Campus Drive'),
        ('Class Room', 'Class Room'),
        ('Lab', 'Lab'),
        ('Mock Interview', 'Mock Interview'),
        ('Placed Students', 'Placed Students'),
    ]
    label = models.CharField(max_length=100, choices=label_choices)
    image = models.ImageField(upload_to='Gallery/')

    def __str__(self):
        return f"{self.label} - {self.id}"

