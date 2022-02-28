from django.db import models
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class student(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)