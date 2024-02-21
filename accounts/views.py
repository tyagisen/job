from .models import User
from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import LoginForm
from django.contrib.auth import authenticate,login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignUpEmployeeForm



class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    # success_url = "/dashboard/"
    def form_valid(self, form):
        email = self.request.POST['email']
        password = self.request.POST['password']
        user =authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            my_user=User.objects.get(email=email)
        
        else:
            return render(
                self.request,
                self.template_name,
                {"error": "Wrong username or password.", "form": form},
            )
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("login"))


class SignUpSuperEmployeeView(CreateView):
    form_class = SignUpEmployeeForm
    template_name='accounts/register.html'
    success_message='Signup successful'
    context_object_name='form'
