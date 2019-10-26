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
            'id':s.id,
            'name':s.first_name + " " +str(s.last_name),
            'gender':s.get_gender_display()
        })
    # return HttpResponse(json.dumps(all_students))
    return render(request=request, template_name='list_student.html', context={'students':all_students})


def mark_attendance(request):
    students = Student.objects.all()
    all_students = []
    for s in students:
        all_students.append({
            'id': s.id,
            'name': s.first_name + " " + str(s.last_name),
            'gender': s.get_gender_display()
        })
    return render(request=request, template_name='mark_attendance.html', context={'students': all_students})


def delete_student(request):
    error = ""
    student_id = request.GET.get('id',None)
    if student_id is None:
        error = "No student id given"
    else:
        try:
            student_obj = Student.objects.get(id = student_id)
            student_obj.delete()
        except Student.DoesNotExist:
            error = "No student with ID:"+student_id+" found!!"

    json_packet = {
        'status': True if error == "" else False,
        'message':error
    }
    return HttpResponse(json.dumps(json_packet), status=200 if error == "" else 500)