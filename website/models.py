from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    course = models.CharField(max_length=500)
    passing_year = models.CharField(max_length=500)


class AptitudeTestRegistration(models.Model):
    name = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to="user/") 


class Result(models.Model):
    user_name = models.CharField(max_length=100)
    correct_answers = models.IntegerField()
    wrong_answers = models.IntegerField()
    total_marks = models.IntegerField()
    def __str__(self):
        return self.user_name