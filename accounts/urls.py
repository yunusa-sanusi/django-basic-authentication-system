from django.urls import path
from accounts.views import create_student, create_teacher, user_dashboard, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
    path('signup/', create_student, name='signup'),
    path('add-teacher/', create_teacher, name='add-teacher'),
    path('dashboard/<int:pk>', user_dashboard, name='dashboard'),
    path('signin/', user_login, name='signin'),
    path('signout/', user_logout, name='signout'),
]
