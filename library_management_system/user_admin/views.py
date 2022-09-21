from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from student.models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def user_admin_index(request):
    data = Book.objects.all()
    return render(request,"user_admin/index.html",{"data":data})

def user_admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=User.objects.get(email=email).username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        messages.info(request,"Login Failed, Please Try Again")     
    return render(request,'user_admin/login.html')


def user_admin_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        experience = request.POST.get('experience')
       
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists!")
                return redirect('user_admin_register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"Email already Exists!")
                    return redirect('user_admin_register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    data = Admin(admin_user = user,experience=experience)
                    data.save()
                    
                    our_user = authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
        else:
            messages.info(request,"Password and Confirm Password Mismatch!")
            return redirect('user_admin_register')
    return render(request,'user_admin/register.html')


def user_admin_logout(request):
    logout(request)
    return redirect('/')

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        book = Book(name=name,author=author,description = description)
        book.save()
        return redirect('/')
    return HTTPResponse("Not Working")

def edit_book(request,pk):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        book = get_object_or_404(Book, pk=pk)
        if book:
            book.name = name 
            book.author = author 
            book.description = description
            book.save()
            return redirect("/")
    return HTTPResponse("Hello")

def delete_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if book:
        book.delete()
        return redirect("/")
    return HTTPResponse("Not Working!")
 
