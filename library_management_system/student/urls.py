from django.urls import path
from . import views
urlpatterns = [
    path("",views.student_index,name="student_index"),
    path("register/",views.student_register,name="student_register"),
    path("login/",views.student_login,name="student_login"),
    path("logout/",views.student_logout,name="student_logout"),
]