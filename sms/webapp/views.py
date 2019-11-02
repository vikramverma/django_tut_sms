from django.shortcuts import render, HttpResponse, redirect
from .forms import StudentForm, LoginForm
from .models import Student, AppUser
import json, time

# Create your views here.
def index(request):
    if check_login(request):
        return render(request=request, template_name='index.html', context={})
    else:
        return HttpResponse("Forbidden Access", status=403)

def add_student(request):
    form = StudentForm
    if request.POST:
        form = StudentForm(request.POST)#, instance=Student)
        if form.is_valid():
            form.save(commit=True)
    return render(request=request, template_name='add_students.html', context={'form':form})

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
    search = request.GET.get('search', None)
    if search:
        students = students.filter(first_name__icontains = search)
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


def check_login(request):
    try:
        if request.session['loggedin']:
            return True
        else:
            return False
    except Exception as e:
        return False

def loginfunction(request):
    error = ""
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        app_user = AppUser.objects.filter(username = username, password=password)
        if app_user.count() > 0:
            request.session['loggedin'] = True
            request.session['loggedin_at'] = int(time.time())
            return redirect('/')
        else:
            error = "Invalid username/password"
    return render(request, template_name='login.html', context={'error':error})


def logoutfunction(request):
    request.session['loggedin'] = False
    return redirect('/login')