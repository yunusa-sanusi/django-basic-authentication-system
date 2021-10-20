from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from accounts.forms import StudentCreationForm, TeacherCreationForm, UserUpdateForm, StudentUpdateForm, TeacherUpdateForm
from accounts.models import Student, Teacher

User = get_user_model()


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard', pk=request.user.pk)

    else:
        return render(request, 'index.html')


# Gets the profile and user details based on the type of user logged in.
def get_profile_details(request, profile):
    if request.user.is_student:
        return StudentUpdateForm(
            request.POST, instance=profile)
    elif request.user.is_teacher:
        return TeacherUpdateForm(
            request.POST, instance=profile)


# gets the dashboard template based on type of logged in user
def get_template(request):
    if request.user.is_student:
        return 'account/student-dashboard.html'
    elif request.user.is_teacher:
        return 'account/teacher-dashboard.html'


@login_required(login_url='signin')
def user_dashboard(request, pk):
    # populating our dashboard form based on logged in usertype
    if request.user.is_student:
        profile = Student.objects.get(user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = StudentUpdateForm(instance=profile)
    elif request.user.is_teacher:
        profile = Teacher.objects.get(user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = TeacherUpdateForm(instance=profile)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = get_profile_details(request, profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard', pk=request.user.pk)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, get_template(request), context)


def create_student(request):
    if request.user.is_authenticated:
        return redirect('dashboard', pk=request.user.pk)
    else:
        form = StudentCreationForm

        if request.method == 'POST':
            form = StudentCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('signin')

        return render(request, 'account/create-student.html', {'form': form})


def create_teacher(request):
    if request.user.is_authenticated:
        return redirect('dashboard', pk=request.user.pk)
    else:
        form = TeacherCreationForm

        if request.method == 'POST':
            form = TeacherCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('signin')

        return render(request, 'account/create-teacher.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard', pk=request.user.pk)
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('dashboard', pk=request.user.pk)

        return render(request, 'account/login.html')


@login_required(login_url='signin')
def user_logout(request):
    logout(request)
    return redirect('home')
