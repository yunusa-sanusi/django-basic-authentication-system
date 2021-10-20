from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import create_student, create_teacher, user_dashboard, user_login, user_logout

urlpatterns = [
    path('signup/', create_student, name='signup'),
    path('add-teacher/', create_teacher, name='add-teacher'),
    path('dashboard/<int:pk>', user_dashboard, name='dashboard'),
    path('login/', user_login, name='signin'),
    path('signout/', user_logout, name='signout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset_form.html'),
         name='password_reset'),

    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'),
         name='password_reset_complete'),
]
