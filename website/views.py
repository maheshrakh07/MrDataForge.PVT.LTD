from django.shortcuts import render ,redirect 
from . import models
from apanel import models as admin_models
# Create your views here.
def home(req):
    all_courses = admin_models.Course.objects.count()
    all_reviews = admin_models.Review.objects.all()
    all_teachers = admin_models.TeamMember.objects.all()
    all_teachers_count = admin_models.TeamMember.objects.count()
    return render(req , "user/index.html", {"all_courses": all_courses, "all_reviews": all_reviews, "all_teachers": all_teachers, "all_teachers_count": all_teachers_count})


def save_enquiry(req):
    if req.method == "POST":
        enq = models.Enquiry(
            name = req.POST.get("name"),
            mobile = req.POST.get("mobile"),
            course = req.POST.get("course"),
            passing_year = req.POST.get("passing_year")
        )
        enq.save()
        return redirect("/")


def about(req):
    return render(req , "user/about.html")


def course(req):
    courses = admin_models.Course.objects.all()
    return render(req , "user/course.html", {"courses": courses})


def Services(req):
    return render(req , "user/Services.html")


def internship(req):
    return render(req , "user/internship.html")


def student_project(req):
    return render(req , "user/student_project.html")


def blog(req):
    return render(req , "user/blog.html")


def gallery(req):
    return render(req , "user/gallery.html")


def contact(req):
    return render(req , "user/contact.html")