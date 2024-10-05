from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True , null=True)
    licence_number = models.CharField(max_length=50 , null=True)
    def __str__(self):
     return f'{self.name} : {self.phone}'