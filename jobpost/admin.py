from django.contrib import admin
from jobpost.models import Job

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_title']