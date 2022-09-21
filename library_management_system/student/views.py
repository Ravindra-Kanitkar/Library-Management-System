from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from student.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def student_index(request):
    books = Book.objects.all()
    return render(request,"student/index.html",{"books":books})

def student_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=User.objects.get(email=email).username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        messages.info(request,"Login Failed, Please Try Again")     
    return render(request,'student/login.html')


def student_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile_no = request.POST.get('mobile_no')
        school_name = request.POST.get('school_name')
      
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists!")
                return redirect('student_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email already Exists!")
                    return redirect('student_register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data = Student(student_user = user,mobile_no=mobile_no,school_name=school_name)
                    data.save()
                    
                    our_user = authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
        else:
            messages.info(request,"Password and Confirm Password Mismatch!")
            return redirect('student_register')
    return render(request,'student/register.html')


def student_logout(request):
    logout(request)
    return redirect('/')