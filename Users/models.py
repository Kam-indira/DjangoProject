from django.db import models

# Create your models here.
class UserDetails(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    place = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    describeYourself = models.CharField(max_length=300)
