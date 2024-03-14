from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from jobpost.models import Job, StarredJob
from rest_framework.filters import SearchFilter
from jobpost.api.serializers import JobListSerializer, JobDetailSerializer, StarredSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django.db.models.query import QuerySet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class JobListAPIView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    filter_backends = [SearchFilter]
    filter = ['job_title']


    # def get_queryset(self):
    #     queryset = self.queryset
    #     if isinstance(queryset, QuerySet):
    #         queryset = queryset.all()
    #         # ata = [{'title': book.title, 'author': book.author, 'is_long': book.is_long} for book in books]
    #         for qs in queryset:
    #             print(qs.change_created_at)

    #         queryset = [
    #             {
    #                'created_at':queryset.created_at,
    #                 'updated_at':queryset.updated_at,
    #                 'created_by':queryset.created_by,
    #                 'updated_by':queryset.updated_by,
    #                 'job_title':queryset.job_title,
    #                 'company_logo':queryset.company_logo,
    #                 'company_name':queryset.company_name,
    #                 'location':queryset.location,
    #                 'post_code':queryset.post_code,
    #                 'job_description':queryset.job_description,
    #                 'pay_rate':queryset.pay_rate,
    #                 'job_image_one':queryset.job_image_one,
    #                 'job_image_two':queryset.job_image_two,
    #                 'job_image_three':queryset.job_image_three,
    #                 'change_created_at':queryset.change_created_at,
    #             }for queryset in queryset
    #         ]
            
    #     return queryset


class JobRetrieveAPIView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
    

class JobPostAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer

    # def get_serializer(self, *args, **kwargs):
    #     """
    #     Return the serializer instance that should be used for validating and
    #     deserializing input, and for serializing output.
    #     """
    #     serializer_class = self.get_serializer_class()


#     if serializer.is_valid():
#     ...
#     return Response(WeatherSerializer(weather).data, status=status.HTTP_201_CREATED)

# print(serializer.errors)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(self.request.user.email)
        serializer.created_by = self.request.user
        serializer.updated_by = self.request.user
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        print(serializer.errors)
    def perform_create(self, serailizer):
        print("fdkldk")
        print(self.request.user)
        serailizer.save(created_by=self.request.user, updated_by=self.request.user)

class StarredCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StarredJob.objects.all()
    serializer_class = StarredSerializer
    

    def get_serializer_context(self, **kwargs):
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

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

    