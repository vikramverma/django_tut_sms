"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url

from .views import index, add_student, list_students, mark_attendance, delete_student

app_name = 'webapp'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add-student$', add_student, name='add-student'),
    url(r'^manage-students$', list_students, name='manage-students'),
    url(r'^mark-attendance$', mark_attendance, name='mark-attendance'),
    url(r'^delete-student$', delete_student, name='delete-student'),
]
