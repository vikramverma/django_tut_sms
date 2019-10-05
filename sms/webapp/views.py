from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request=request, template_name='index.html', context={})

def add_student(request):
    return render(request=request, template_name='add_students.html', context={})