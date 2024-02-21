from django import forms
from accounts.models import (
    SUPER_ADMIN,
    ADMIN,
    EMPLOYEER,
    EMPLOYEE
)
from accounts.models import User
from django.contrib.auth.models import Group



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
    role = forms.ChoiceField(choices=role_choices, required=True)
    groups= forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("Confirm New password"),
                                    widget=forms.PasswordInput)

    class Meta:
        model= User 
        fields = ['username', 'new_password1', 'new_password2', 'role', 'groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['groups'].widget.attrs.update({'class': 'form-control'})
        self.fields["new_password1"].widget.attrs.update(
            {'placeholder': 'New Password', 'required': 'true'})
        self.fields["new_password2"].widget.attrs.update(
            {'placeholder': 'Confirm New Password', 'required': 'true'})


    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1!=password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code = 'password_missmatch'
                )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        print(user)
        user.set_password(self.cleaned_data["new_password2"])
        if commit:
            user.save()
        if self.cleaned_data['groups']:
            user.groups.add(self.cleaned_data['groups'])
        return user


class SignUpEmployeeForm(SignUpEmployee):
    role_choices=(
        (EMPLOYEE, 'Employee')
    )
    role = forms.ChoiceField(choices=role_choices, required=True)
    