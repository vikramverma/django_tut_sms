from django.db import models


# Create your models here.
class Student(models.Model):
    gender_choices = ((1, 'Male'),(2, 'Female'))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, default='', blank=True)
    gender = models.IntegerField(max_length=10, choices=gender_choices)
    husband_name = models.CharField(max_length=50, null=True, blank=True, default='')
    fathers_name = models.CharField(max_length=50, null=True, blank=True, default='')

    def __str__(self):
        return self.first_name

    # def get_gender(self):
    #     return self.gender_choices.__getitem__(self.gender)


class Mobile(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number


class AppUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username