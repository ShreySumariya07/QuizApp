from django.db import models 
from django.contrib.auth.models import AbstractUser
#
# from django.utils.translation import ugettext_lazy as _ 
# from django.conf import settings 


class User(AbstractUser): 
    phone_no = models.IntegerField()
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    b_day = models.DateField(null=False, blank=False)
    grade = models.IntegerField(null = False)
    age = models.IntegerField(null=False)
    # def age(self):
    #     import datetime
    #     return int((datetime.datetime.now() - self.b_day).days / 365.25  )
    # age = property(age)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=300,null= False)
    subject = models.CharField(max_length=100,null=False)


    