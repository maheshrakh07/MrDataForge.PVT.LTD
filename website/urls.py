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
    path('save_enquiry/' , views.save_enquiry , name="save_enquiry"),
    path('apptitude_test/' , views.apptitude_test , name="apptitude_test"),
    path('aptitude_register/' , views.aptitude_register , name="aptitude_register"),
    path('apti_login/' , views.apti_login , name="apti_login"),
    path('apti_logout/' , views.apti_logout , name="apti_logout"),
    path('appti_profile/' , views.apti_profile , name="apti_profile"),
    path('test/' , views.test , name="test"),   
    path('submit_test/' , views.submit_test , name="submit_test"),
    # path('results/' , views.show_results , name="results"),
    path('show_results/' , views.show_results , name="show_results"),
    

]
