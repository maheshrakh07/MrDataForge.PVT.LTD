import os

from django.shortcuts import render , redirect
from website import models as user
from . import models
from django.db.models import Count
# Create your views here.


def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        if username == "rakh0745@gmail.com" and password == "rakh0745":
            req.session["admin"] = username
            req.session["admin_logged_in"] = True
            return redirect("/admin/home")      
    return render(req, "admin/login.html")

def home(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    all_courses = models.Course.objects.count()
    apti_user = user.AptitudeTestRegistration.objects.all()
    return render(req, "admin/index.html", {"all_courses": all_courses, "apti_user": apti_user})

def registration_list(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
    reg_list = user.Enquiry.objects.all()
    return render(req , "admin/registration_list.html", {"reg_list":reg_list})


def course(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
    courses = models.Course.objects.all()
    return render(req, "admin/course.html", {"courses": courses})


def save_course(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
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
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
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
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
    course = models.Course.objects.get(id=course_id)
    image_path = course.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    course.delete()
    return redirect("/admin/course")


def reviews(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
    reviews = models.Review.objects.all()
    return render(req, "admin/reviews.html", {"reviews": reviews})

def internship(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    
    return render(req, "admin/internship.html")

def projects(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    return render(req, "admin/projects.html")

def blogs(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login") 
    return render(req, "admin/blogs.html")

def gallery(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    return render(req, "admin/gallery.html")

def save_review(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login") 
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
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
        
    review = models.Review.objects.get(id=review_id)
    image_path = review.reviewer_image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    review.delete()
    return redirect("/admin/reviews")


def team(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    team_members = models.TeamMember.objects.all()
    return render(req, "admin/team.html", {"team_members": team_members})

def save_team_member(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
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
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    team_member = models.TeamMember.objects.get(id=member_id)
    return render(req, "admin/edit_team_member.html", {"team_member": team_member})

def update_team_member(req, member_id):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login") 
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
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    team_member = models.TeamMember.objects.get(id=member_id)
    image_path = team_member.image.path
    if os.path.exists(image_path):
        os.remove(image_path)
    team_member.delete()
    return redirect("/admin/team")


def question_paper(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login") 
    questions = models.QuestionPaper.objects.all()
    return render(req, "admin/question_paper.html", {"questions": questions})   



def add_question(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    if req.method == "POST":
        question = req.POST.get("question")
        option_1 = req.POST.get("option_1")
        option_2 = req.POST.get("option_2")
        option_3 = req.POST.get("option_3")
        option_4 = req.POST.get("option_4")
        answer = req.POST.get("answer")
        marks = req.POST.get("marks")

        question_obj = models.QuestionPaper(
            quetion=question,
            option_1=option_1,
            option_2=option_2,
            option_3=option_3,
            option_4=option_4,
            answer=answer,
            marks=marks
         )
        question_obj.save()
    return redirect("/admin/question_paper")

def delete_question(req, question_id):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login") 
    question = models.QuestionPaper.objects.get(id=question_id)
    question.delete()
    return redirect("/admin/question_paper")


def results(req):

    if not req.session.get("admin_logged_in"):

        return redirect("/admin/login")

    results = user.Result.objects.values(

        "user_name"

    ).annotate(

        total_attempts=Count("id")

    )

    return render(

        req,

        "admin/apti_result.html",

        {

            "results": results

        }

    )



def apti_regi_list(req):
    if not req.session.get("admin_logged_in"):
        return redirect("/admin/login")
    registrations = user.AptitudeTestRegistration.objects.all()
    return render(req, "admin/apti_user_list.html", {"registrations": registrations})

def student_attempts(req,name):

    if not req.session.get("admin_logged_in"):

        return redirect("/admin/login")

    attempts = user.Result.objects.filter(

        user_name=name

    ).order_by("-id")

    return render(

        req,

        "admin/student_attempts.html",

        {

            "attempts": attempts,

            "student_name": name

        }

    )