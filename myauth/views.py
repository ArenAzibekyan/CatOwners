from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect, render


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup_done')
    template_name = 'auth/signup.html'


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name = 'auth/password_change.html'


class PasswordChangeDone(TemplateView):
    template_name = 'auth/password_change_done.html'


@login_required
def UserDelete(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(username=request.user.username)
            user.delete()
        except Exception as e:
            print(e.args)
            return render(request=request, template_name='auth/user_delete_failed.html')
        else:
            return render(request=request, template_name='auth/user_delete_done.html')
    else:
        return redirect('home')