from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from jobpost.models import Job, StarredJob
from .forms import JobCreateForm
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class HomePage(TemplateView, LoginRequiredMixin):
    
    template_name = 'jobpost/dashboard.html'



class JobListView(ListView):
    template_name = 'jobpost/getjobs.html'
    model = Job
    context_object_name = 'jobs'



class JobDetailView(DetailView):
    model = Job
    context_object_name='detail'
    template_name = 'jobpost/job_detail.html'



        # primary key is located in kwargs
        # pk =self.kwargs.get('pk')
        # x =Job.objects.get(pk=pk)
        # print(x.created_at)


    def get_context_data(self, **kwargs):
        '''
        For accessing primary key here.
        pk = self.kwargs.get('pk')

        for accessing the value of certain field. for example below i am extracting value of created_at to modify and sent to template
        context['detail'].created_at
        '''
        context = super().get_context_data(**kwargs)
        posted_date = context['detail'].created_at.date()
        today_date = datetime.now().date()
        passed_date=today_date-posted_date
        if passed_date==today_date:
            context['date'] = 'Recently Added'
        else:
            passed_date=str(passed_date).split(', ')[0]
            context['date']=passed_date
        
        context['page_name'] ='Detail Page' 
        return context
    


class AddJobForm(CreateView):
    template_name = 'jobpost/create_job.html'
    form_class = JobCreateForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            print("valid")
            return self.form_valid(form)
        else:
            print("invalid")
            return self.form_invalid(form)


class StarredCreateView(CreateView):
    model = StarredJob

    

   

    