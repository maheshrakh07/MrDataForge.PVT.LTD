import os

from django.shortcuts import render , redirect
from website import models as user
from . import models
# Create your views here.


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        if username == "admin@gmail.com" and password == "admin123":
            return redirect("/admin/home")
    return render(req, "admin/login.html")

def home(req):
    all_courses = models.Course.objects.count()
    return render(req, "admin/index.html", {"all_courses": all_courses})

def registration_list(req):
    reg_list = user.Enquiry.objects.all()
    return render(req , "admin/registration_list.html", {"reg_list":reg_list})


def course(req):
    courses = models.Course.objects.all()
    return render(req, "admin/course.html", {"courses": courses})


def save_course(req):
    if req.method == "POST":
        name = req.POST.get("course_name")
        description = req.POST.get("course_description")
        price = req.POST.get("course_price")
        key_point_1 = req.POST.get("key_point_1")
        key_point_2 = req.POST.get("key_point_2")
        key_point_3 = req.POST.get("key_point_3")
        key_point_4 = req.POST.get("key_point_4")
        key_point_5 = req.POST.get("key_point_5")
        duration = req.POST.get("course_duration")
        image = req.FILES.get("course_image")

        course_obj = models.Course(
            name=name,
            description=description,
            price=price,
            key_point_1=key_point_1,
            key_point_2=key_point_2,
            key_point_3=key_point_3,
            key_point_4=key_point_4,
            key_point_5=key_point_5,
            duration=duration,
            image=image
        )
        course_obj.save()
    return redirect("/admin/course")

def edit_course(req, course_id):
    course = models.Course.objects.get(id=course_id)
    if req.method == "POST":
        course.name = req.POST.get("course_name")
        course.description = req.POST.get("course_description")
        course.price = req.POST.get("course_price")
        course.key_point_1 = req.POST.get("key_point_1")
        course.key_point_2 = req.POST.get("key_point_2")
        course.key_point_3 = req.POST.get("key_point_3")
        course.key_point_4 = req.POST.get("key_point_4")
        course.key_point_5 = req.POST.get("key_point_5")
        course.duration = req.POST.get("course_duration")
        if "course_image" in req.FILES:
            course.image = req.FILES["course_image"]
        course.save()
        return redirect("/admin/course")
    return render(req, "admin/edit_course.html", {"course": course})

def delete_course(req, course_id):
    course = models.Course.objects.get(id=course_id)
    image_path = course.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    course.delete()
    return redirect("/admin/course")


def reviews(req):
    reviews = models.Review.objects.all()
    return render(req, "admin/reviews.html", {"reviews": reviews})

def internship(req):
    return render(req, "admin/internship.html")

def projects(req):
    return render(req, "admin/projects.html")

def blogs(req):
    return render(req, "admin/blogs.html")

def gallery(req):
    return render(req, "admin/gallery.html")

def save_review(req):
    if req.method == "POST":
        reviewer_name = req.POST.get("reviewer_name")
        review_text = req.POST.get("review_text")
        review_rating = req.POST.get("review_rating")
        reviewer_position = req.POST.get("reviewer_position")
        reviewer_image = req.FILES.get("reviewer_image")

        review_obj = models.Review(
            reviewer_name=reviewer_name,
            review_text=review_text,
            review_rating=review_rating,
            reviewer_position=reviewer_position,
            reviewer_image=reviewer_image
        )
        review_obj.save()
    return redirect("/admin/reviews")

def delete_review(req, review_id):
    review = models.Review.objects.get(id=review_id)
    image_path = review.reviewer_image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    review.delete()
    return redirect("/admin/reviews")


def team(req):
    team_members = models.TeamMember.objects.all()
    return render(req, "admin/team.html", {"team_members": team_members})

def save_team_member(req):
    if req.method == "POST":
        name = req.POST.get("name")
        position = req.POST.get("position")
        mobile = req.POST.get("mobile")
        email = req.POST.get("email")
        facebook_link = req.POST.get("facebook_link")
        linkedin_link = req.POST.get("linkedin_link")
        instagram_link = req.POST.get("instagram_link")
        salary = req.POST.get("salary")
        qualification = req.POST.get("qualification")
        experience = req.POST.get("experience")
        dob = req.POST.get("dob")
        password = req.POST.get("password")
        image = req.FILES.get("photo")
        bio = req.POST.get("bio")

        team_member_obj = models.TeamMember(
            name=name,
            position=position,
            mobile=mobile,
            email=email,
            facebook_link=facebook_link,
            linkedin_link=linkedin_link,
            instagram_link=instagram_link,
            salary=salary,
            qualification=qualification,
            experience=experience,
            dob=dob,
            password=password,
            image=image,
            bio=bio
        )
        team_member_obj.save()
    return redirect("/admin/team")

def edit_team_member(req, member_id):
    team_member = models.TeamMember.objects.get(id=member_id)
    return render(req, "admin/edit_team_member.html", {"team_member": team_member})

def update_team_member(req, member_id):
    team_member = models.TeamMember.objects.get(id=member_id)
    if req.method == "POST":
        team_member.name = req.POST.get("name")
        team_member.position = req.POST.get("position")
        team_member.mobile = req.POST.get("mobile")
        team_member.email = req.POST.get("email")
        team_member.facebook_link = req.POST.get("facebook_link")
        team_member.linkedin_link = req.POST.get("linkedin_link")
        team_member.instagram_link = req.POST.get("instagram_link")
        team_member.salary = req.POST.get("salary")
        team_member.qualification = req.POST.get("qualification")
        team_member.experience = req.POST.get("experience")
        team_member.dob = req.POST.get("dob")
        team_member.password = req.POST.get("password")
        team_member.bio = req.POST.get("bio")
        if "photo" in req.FILES:
            team_member.image = req.FILES["photo"]
        team_member.save()
    return redirect("/admin/team")

def delete_team_member(req, member_id):
    team_member = models.TeamMember.objects.get(id=member_id)
    image_path = team_member.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    team_member.delete()
    return redirect("/admin/team")
