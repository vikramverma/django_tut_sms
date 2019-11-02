from django.forms import ModelForm
# from django.forms import forms
from .models import Student, AppUser


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name', 'gender'] #'__all__'


class LoginForm(ModelForm):
    class Meta:
        model = AppUser
        fields = '__all__'

#
# class DemoForm(forms):
#     name = formsm