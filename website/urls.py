from django.urls import path
from . import views 


urlpatterns = [
    path('' , views.home , name="home"),
    path('about/' , views.about , name="about"),
    path('course/' , views.course , name="course"),
    path('Services/' , views.Services , name="Services"),
    path('internship/' , views.internship , name="internship"),
    path('student_project/' , views.student_project , name="student_project"),
    path('blog/' , views.blog , name="blog"),
    path('gallery/' , views.gallery , name="gallery"),
    path('contact/' , views.contact , name="contact"),
    path('save_enquiry/' , views.save_enquiry , name="save_enquiry")

]
