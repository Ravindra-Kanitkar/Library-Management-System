from django.shortcuts import render,redirect
from student.models import *
def index(request):
    if request.user.is_authenticated == True and Student.objects.filter(student_user=request.user).exists():
        return redirect("student_index")
    elif request.user.is_authenticated == True and Admin.objects.filter(admin_user=request.user).exists():
        return redirect("user_admin_index")
    
    return render(request,"main/index.html")