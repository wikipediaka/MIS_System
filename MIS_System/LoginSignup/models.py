from django.db import models

# Create your models here.

class Accounts(models.Model):
    Id_Number = models.CharField(max_length=10, primary_key=True)
    Status = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Contact = models.IntegerField()
    Password = models.CharField(max_length=25)
