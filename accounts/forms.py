from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import Student, Teacher, User


class StudentCreationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user


class TeacherCreationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder': 'Confirm Password'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        Teacher.objects.create(user=user)
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username')


class StudentUpdateForm(forms.ModelForm):
    LEVEL_CHOICES = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )

    age = forms.IntegerField(
        label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age', 'min': 18}))
    matric_number = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matric Number'}))
    phone_number = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('age', 'matric_number', 'phone_number', 'level')


class TeacherUpdateForm(forms.ModelForm):
    TITLE_CHOICES = (
        ('Dr', 'Dr'),
        ('Mr', 'Mr'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Prof', 'Prof'),
    )

    phone_number = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    staff_id = forms.CharField(
        label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    title = forms.ChoiceField(choices=TITLE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Teacher
        fields = ('title', 'phone_number', 'staff_id')
