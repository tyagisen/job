from django import forms
from accounts.models import (
    SUPER_ADMIN,
    ADMIN,
    EMPLOYEER,
    EMPLOYEE
)
from accounts.models import User
# from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    


class SignUpEmployee(forms.ModelForm):
    role_choices = (
        (SUPER_ADMIN,"Super Admin"),
        (ADMIN, "Admin"),
        (EMPLOYEER, "Employeer"),
        (EMPLOYEE, "Employee")
    )
    first_name= forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # role = forms.ChoiceField(choices=role_choices, required=True)
    # groups= forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    # error_messages = {
    #     'password_mismatch': ("The two password fields didn't match."),
    # }
    # password1 = forms.CharField(label=("New password"),
    #                                 widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Confirm New password"),
                                    widget=forms.PasswordInput)

    class Meta:
        model= User 
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        # self.fields['groups'].widget.attrs.update({'class': 'form-control'})
        self.fields["password"].widget.attrs.update(
            {'placeholder': 'New Password', 'required': 'true'})
        self.fields["password2"].widget.attrs.update(
            {'placeholder': 'Confirm New Password', 'required': 'true'})

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        print(password1, password2)
        if password1 and password2:
            if password1!=password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code = 'password_missmatch'
                )
        return password2

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        check = User.objects.filter(email=email)
        if check.count():
            raise ValidationError("Email Already exists.")
        print(email)
        return email

class SignUpEmployeeForm(SignUpEmployee):
    pass
    # role_choices=(
    #     (EMPLOYEE, 'Employee')
    # )
    # def save(self, commit=True):
    #     print("abc")
    #     user = User.objects.create(
    #         email=self.cleaned_data['email'],
    #         first_name=self.cleaned_data['first_name'],
    #         last_name= self.cleaned_data['last_name'],
    #         # role = EMPLOYEE,
    #         password = self.cleaned_data['password2']
    #     )
    #     return user