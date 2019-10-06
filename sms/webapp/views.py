from django.shortcuts import render, HttpResponse

from .models import Student
import json

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html', context={})

def add_student(request):
    return render(request=request, template_name='add_students.html', context={})

def list_students(request):
    #
    # #select all from table
    students = Student.objects.all()
    # #select all from table where gender = 1
    # students = Student.object.filter(gender = 1)
    # # select all from table where gender <> 1
    # students = Student.object.exclude(gender=1)
    #
    # #returns a list of objects
    # student = Student.objects.get(id = 1)
    # #single object
    #
    all_students = []
    for s in students:
        all_students.append({
            'name':s.first_name + " " +str(s.last_name),
            'gender':s.gender
        })
    # return HttpResponse(json.dumps(all_students))
    return render(request=request, template_name='list_student.html', context={'students':all_students})