from django.db import models
#we need to save
class Car(models.Model):
   id = models.AutoField(primary_key=True)
   car_name = models.CharField(max_length=64,unique=True)
   image = models.ImageField(upload_to='images')
   description = models.CharField(max_length=300)

