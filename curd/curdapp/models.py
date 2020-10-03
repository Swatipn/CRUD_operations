from django.db import models

# Create your models here.
class Student(models.Model):
    USN = models.IntegerField()
    Name = models.CharField(max_length=50)
    Marks = models.IntegerField()
    cgpa = models.FloatField()
    