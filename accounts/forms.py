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
