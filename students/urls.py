from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("api/students/", views.get_students,name="get_students"),
    path("api/students/add/", views.add_student,name="add_student"),
    path("api/students/delete/<int:id>/", views.delete_student,name="delete_student"),
]
