from django.db import models 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(null=False, unique=True)
    phone_no = models.IntegerField()
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_no', 'is_teacher', 'is_student']
'''
    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
'''


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    b_day = models.DateField(null=False, blank=False)
    grade = models.IntegerField(null=False)
    age = models.IntegerField(null=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=300, null=False)
    subject = models.CharField(max_length=100, null=False)
