from rest_framework import serializers
from jobpost.models import Job, StarredJob


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'job_title',
            'company_logo',
            'company_name',
            'location',
            'post_code',
            'job_description',
            'pay_rate',
            'change_created_at'

        )

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
            'job_title',
            'company_logo',
            'company_name',
            'location',
            'post_code',
            'job_description',
            'pay_rate',
            'job_image_one',
            'job_image_two',
            'job_image_three',
        )


class StarredSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarredJob
        fields = [

            'user',
            'job'
        ]