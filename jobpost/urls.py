from django.urls import path
from jobpost.views import JobListView, HomePage, AddJobForm, JobDetailView

urlpatterns =[
    path('dashboard/', HomePage.as_view(), name='home'),
    path('', JobListView.as_view(), name='job-list'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('add-job/', AddJobForm.as_view(), name='job-add')
]