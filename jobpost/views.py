from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from jobpost.models import Job
from .forms import JobCreateForm
from datetime import datetime, timedelta


class HomePage(TemplateView):
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
        print(passed_date)
        if passed_date:
            context['date'] = 'Recently Added'
        else:
            context['date']=passed_date
        
        context['page_name'] ='Detail Page' 
        return context
    


class AddJobForm(CreateView):
    template_name = 'jobpost/create_job.html'
    # model = Job
    form_class = JobCreateForm
    success_url = 'job/add-job/'
    # fields= ['job_title', 'company_logo', 'company_name', 'location', 'post_code','job_description', 'pay_rate', 'job_image_one', 'job_image_two', 'job_image_three']
    # fields='__all__'

    def form_valid(self, form):
        self.object = form.save()
        print(self.object)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("reifdiejkd")
        return self.render_to_response(self.get_context_data(form=form))
    