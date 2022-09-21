from django.urls import path
from . import views
urlpatterns = [
    path("",views.user_admin_index,name="user_admin_index"),
    path("register/",views.user_admin_register,name="user_admin_register"),
    path("login/",views.user_admin_login,name="user_admin_login"),
    path("logout/",views.user_admin_logout,name="user_admin_logout"),
    path("add_book",views.add_book,name="add_book"),
    path("edit_book/<int:pk>/",views.edit_book,name="edit_book"),
    path("delete_book/<int:pk>/",views.delete_book,name="delete_book"),
]