from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Student(models.Model):
    student_user = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    
    mobile_no = models.CharField(max_length=12,blank=True)
    school_name = models.CharField(max_length=200,blank=True)
    
class Admin(models.Model):
    admin_user = models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default=0)
    
class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    description = models.TextField()
    
    