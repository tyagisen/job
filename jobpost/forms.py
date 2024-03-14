from django import forms
from jobpost.models import Job

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields='__all__'
