from django.contrib import admin

# Register your models here.
from .models import Student, Mobile
admin.site.register(Student)
admin.site.register(Mobile)