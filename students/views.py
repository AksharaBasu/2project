from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
import json

def home(request):
    return render(request,"index.html")

def get_students(request):
    students = Student.objects.all()
    data=[]
    for student in students:
        data.append({
            "id":student.id,
            "name":student.name,
            "email":student.email,
            "course":student.course,
        })
    return JsonResponse(data,safe=False)

def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Student.objects.create(
            name=data["name"],
            email=data["email"],
            course=data["course"]
        )
        return JsonResponse({ "message":"Student added successfully!"})

def delete_student(request):
    if request.method == "DELECT":
        student = Student.objects.get( id=id)
        student.delete()
        return JsonResponse({ "message": "Student deleted successfilly!"})
    
