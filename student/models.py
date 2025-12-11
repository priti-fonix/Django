from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='images')
    batch = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


