from django import forms
from jobpost.models import Job

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(JobCreateForm, self).__init__()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    

   