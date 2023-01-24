from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from studentapp.models import City, Course, Student


# Create your views here.
def reg_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):
    user_name = request.POST['txtusername']
    user_email = request.POST['txtemail']
    user_pswd = request.POST['txtpswd']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html',{'data':'username,email and password already exists'})
    else:
        u1 = User.objects.create_superuser(username = user_name,email = user_email,password = user_pswd)
        u1.save()
        return redirect('log')


def log_fun(request):

    return render(request, 'login.html',{'data':''})


def logdata_fun(request):
    uname = request.POST['txtusername']
    upassword = request.POST['txtpswd']
    user1 = authenticate(username=uname,password=upassword)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'user is not a super user'})
    else:
        return render(request, 'login.html', {'data': 'enter proper username and password'})


def home_fun(request):
    return render(request,'home.html')


def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'add_students.html',{'city_data': city , 'course_data': course})


def readdata_fun(request):
    s1 = Student()
    s1.student_name = request.POST['txtusername']
    s1.student_age = request.POST['tbage']
    s1.student_phno = request.POST['tbphno']
    s1.student_city = City.objects.get(city_name=request.POST['ddlcity'])
    s1.student_course = Course.objects.get(course_name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')


def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data':s1})


def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()

    if request.method == 'POST':
        s1.student_name = request.POST['txtusername']
        s1.student_age = request.POST['tbage']
        s1.student_phno = request.POST['tbphno']
        s1.student_city = City.objects.get(city_name=request.POST['ddlcity'])
        s1.student_course = Course.objects.get(course_name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')

    return render(request,'update.html',{'data':s1 , 'city_data':city,'course_data':course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')