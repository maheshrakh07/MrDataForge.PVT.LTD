from django.shortcuts import render ,redirect 
from . import models
from apanel import models as admin_models
from django.core.paginator import Paginator
from django.http import HttpResponse
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


def apptitude_test(req):
    return render(req , "user/apptitude_test.html")


def aptitude_register(req):
    if req.method == "POST":
        name = req.POST.get("name")
        mobile = req.POST.get("mobile")
        email = req.POST.get("email")
        gender = req.POST.get("gender")
        password = req.POST.get("password") 
        photo = req.FILES.get("photo")
       
        registration = models.AptitudeTestRegistration(
            name=name,
            mobile=mobile,
            email=email,
            gender=gender,
            password=password,
            photo=photo 
        )
        registration.save()
        return redirect("/apti_login/")
    


def apti_login(req):
    if req.method == "POST":
        email = req.POST.get("email")
        password = req.POST.get("password")
        
        login = models.AptitudeTestRegistration.objects.filter(email=email, password=password).first()
        if login:
            req.session['user_id'] = login.id
            req.session['user_name'] = login.name
            return redirect("/appti_profile/")
        else:
            return render(req , "user/apti_login.html", {"error": "Invalid email or password"})
    return render(req , "user/apti_login.html")

def apti_logout(req):
    req.session.flush()
    return redirect("/apti_login/")

def apti_profile(req):
    if not req.session.get('user_id'):
        return redirect("/apti_login/")
    profile = models.AptitudeTestRegistration.objects.get(id=req.session.get('user_id'))
    total_attempts = models.Result.objects.filter(user_name=profile.name).count()
    profile.total_attempts = total_attempts 
    return render(req , "user/apti_profile.html", {"profile": profile})



def test(req):
    if not req.session.get('user_id'):
        return redirect("/apti_login/")
    apti_profile = models.AptitudeTestRegistration.objects.get(id=req.session.get('user_id'))


    # all_questions = admin_models.QuestionPaper.objects.all()
    all_questions =admin_models.QuestionPaper.objects.all().order_by('?')
    paginator = Paginator(all_questions, 50)

    page_number = req.GET.get('page')

    paper = paginator.get_page(page_number)

    return render(
        req,
        "user/test.html",
        {
            "paper": paper,
            "profile": apti_profile
        }
    )


def submit_test(req):

    if not req.session.get('user_id'):

        return redirect("/apti_login/")

    if req.method == "POST":

        questions = admin_models.QuestionPaper.objects.all()

        total_marks = 0

        correct_answers = 0

        wrong_answers = 0

        attempted = 0

        not_attempted = 0

        result_data = []

        # LOGIN USER
        user_id =req.session.get("user_id")

        user =models.AptitudeTestRegistration.objects.get(
            id=user_id
        )

        for question in questions:

            selected_answer =req.POST.get(
                f"selected_ans{question.id}"
            )

            is_correct = False

            # NOT ATTEMPTED
            if not selected_answer:

                not_attempted += 1

            else:

                attempted += 1

            # CHECK ANSWER
            if selected_answer == question.answer:

                total_marks += question.marks

                correct_answers += 1

                is_correct = True

            else:

                wrong_answers += 1

            # STORE QUESTION RESULT
            result_data.append({

                "question":
                question.quetion,

                "selected":
                selected_answer,

                "correct":
                question.answer,

                "is_correct":
                is_correct,

                "marks":
                question.marks

            })

        # SAVE RESULT DATABASE
        models.Result.objects.create(

            user_name=user.name,

            correct_answers=correct_answers,

            wrong_answers=wrong_answers,

            total_marks=total_marks

        )

        return render(

            req,

            "user/result.html",

            {

                "total_marks":
                total_marks,

                "correct_answers":
                correct_answers,

                "wrong_answers":
                wrong_answers,

                "attempted":
                attempted,

                "not_attempted":
                not_attempted,

                "results":
                result_data

            }

        )
    
# def show_results(req):
#     results = models.Result.objects.all()
#     return render(req , "user/show_results.html", {"results": results})

def show_results(req):

    # LOGIN CHECK
    if not req.session.get("user_id"):

        return redirect("/apti_login/")

    # LOGIN USER ID
    user_id =req.session.get("user_id")

    # LOGIN USER
    profile =models.AptitudeTestRegistration.objects.get(
        id=user_id
    )

    # ONLY LOGIN USER RESULTS
    results =models.Result.objects.filter(
        user_name=profile.name
    )

    return render(
        req,
        "user/show_results.html",
        {

            "results":results,

            "profile":profile

        }
    )