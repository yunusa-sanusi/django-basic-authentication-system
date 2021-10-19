from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import StudentCreationForm, TeacherCreationForm


def index(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    else:
        return render(request, 'index.html')


@login_required(login_url='accounts:signin')
def user_dashboard(request):
    return render(request, 'account/dashboard.html')


def create_student(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    else:
        form = StudentCreationForm

        if request.method == 'POST':
            form = StudentCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('accounts:signin')

        return render(request, 'account/create-student.html', {'form': form})


def create_teacher(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    else:
        form = TeacherCreationForm

        if request.method == 'POST':
            form = TeacherCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('accounts:signin')

        return render(request, 'account/create-teacher.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')

        return render(request, 'account/login.html')


@login_required(login_url='accounts:signin')
def user_logout(request):
    logout(request)
    return redirect('home')
