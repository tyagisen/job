from django.contrib import admin
from jobpost.models import Job, StarredJob

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_title']

@admin.register(StarredJob)
class StarredAdmin(admin.ModelAdmin):
    list_display = ["user", "job"]