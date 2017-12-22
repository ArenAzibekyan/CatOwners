from django.urls import path
from . import views as myViews
from django.contrib.auth import views as authViews
from django.views.generic.base import TemplateView


urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),

    path('signup/', myViews.SignUp.as_view(), name='signup'),
    path('signup_done/', TemplateView.as_view(template_name='auth/signup_done.html'), name='signup_done'),

    path('password_change/', myViews.PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', myViews.PasswordChangeDone.as_view(), name='password_change_done'),

    path('user_delete/', myViews.UserDelete),
]