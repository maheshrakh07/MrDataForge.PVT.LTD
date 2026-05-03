from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    course = models.CharField(max_length=500)
    passing_year = models.CharField(max_length=500)