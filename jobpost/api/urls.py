from django.urls import path
from jobpost.api.views import JobListAPIView, JobRetrieveAPIView, JobPostAPIView, StarredCreateAPIView

urlpatterns = [
    path('list', JobListAPIView.as_view(), name='api-job-list'),
    path('detail/<int:pk>/', JobRetrieveAPIView.as_view(), name='api-job-detail'),
    path('create', JobPostAPIView.as_view(), name='api-job-create'),
    path('starred/create', StarredCreateAPIView.as_view(), name='starred-job')
]