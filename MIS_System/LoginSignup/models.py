from django.db import models

# Create your models here.

class Accounts(models.Model):
    Id_Number = models.CharField(max_length=20, primary_key=True)
    Status = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Full_Name = models.CharField(max_length=100)
    Email = models.TextField(max_length=100)
    Contact = models.BigIntegerField()
    Password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.Full_Name
    
