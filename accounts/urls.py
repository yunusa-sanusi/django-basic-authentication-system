from django.urls import path
from accounts.views import create_student, user_dashboard, user_login, user_logout

app_name = 'accounts'

urlpatterns = [
    path('signup/', create_student, name='signup'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('signin/', user_login, name='signin'),
    path('signout/', user_logout, name='signout'),
]
