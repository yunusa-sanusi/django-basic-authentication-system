from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Student(models.Model):
    LEVEL_CHOICES = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=12, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    age = models.IntegerField(default=18, null=True)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(models.Model):
    TITLE_CHOICES = (
        ('Dr', 'Dr'),
        ('Mr', 'Mr'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Prof', 'Prof'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True)
    title = models.CharField(max_length=5, choices=TITLE_CHOICES, null=True)
    staff_id = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
