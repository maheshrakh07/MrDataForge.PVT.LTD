from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/admin/images/') 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    key_point_1 = models.CharField(max_length=255)
    key_point_2 = models.CharField(max_length=255)
    key_point_3 = models.CharField(max_length=255)
    key_point_4 = models.CharField(max_length=255)
    key_point_5 = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
    
class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_text = models.TextField()
    review_rating = models.CharField(max_length=10)
    reviewer_position = models.CharField(max_length=100)
    reviewer_image = models.ImageField(upload_to='static/admin/images/', null=True, blank=True)

    def __str__(self):
        return self.reviewer_name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/admin/images/')
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    facebook_link = models.URLField(max_length=200, blank=True)
    linkedin_link = models.URLField(max_length=200, blank=True)
    instagram_link = models.URLField(max_length=200, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    dob = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    bio = models.TextField(default="")
    def __str__(self):
        return self.name