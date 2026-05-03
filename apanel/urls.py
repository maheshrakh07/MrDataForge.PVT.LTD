from django.urls import path
from . import views



urlpatterns = [
    path('' , views.login , name="login"),
    path('logout/' , views.logout , name="logout"),
    path('home/' , views.home , name="home"),
    path('registration_list/' , views.registration_list , name="registration_list"),
    path('course/' , views.course , name="course"),
    path('save_course/' , views.save_course , name="save_course"),
    path('edit_course/<int:course_id>/', views.edit_course, name="edit_course"),
    path('delete_course/<int:course_id>/', views.delete_course, name="delete_course"),
    path('reviews/' , views.reviews , name="reviews"),
    path('internship/' , views.internship , name="internship"),
    path('projects/' , views.projects , name="projects"),
    path('blogs/' , views.blogs , name="blogs"),
    path('gallery/' , views.gallery , name="gallery"),
    path('save_review/' , views.save_review , name="save_review"),
    path('delete_review/<int:review_id>/', views.delete_review, name="delete_review"),
    path('team/' , views.team , name="team"),
    path('save_team_member/' , views.save_team_member , name="save_team_member"),
    path('edit_team_member/<int:member_id>/', views.edit_team_member, name="edit_team_member"),
    path('delete_team_member/<int:member_id>/', views.delete_team_member, name="delete_team_member"),
    path('update_team_member/<int:member_id>/', views.update_team_member, name="update_team_member"),
]
