from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Resume=models.FileField(upload_to='files/')
    Photo=models.ImageField(upload_to='images/')
    Password=models.CharField(max_length=50)
