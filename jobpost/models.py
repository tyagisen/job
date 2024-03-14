from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()


# flag = (
#     ('inprogress', 'inprogress'),
#     ('starred', 'starred')
# )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator_%(class)ss")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updater_%(class)ss")

    class Meta:
        abstract=True


class Job(BaseModel):
    job_title= models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to="logo", null=True, blank=True)
    company_name= models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    post_code = models.CharField(max_length=50)
    job_description = RichTextField(max_length=2000)
    pay_rate = models.CharField(default="£",max_length=50)
    job_image_one = models.ImageField(upload_to='job_image', null=True, blank=True)
    job_image_two = models.ImageField(upload_to='job_image', null=True, blank=True)
    job_image_three = models.ImageField(upload_to='job_image', null=True, blank=True)
    # job_type = models.CharField(max_length=70, choices=flag, default='inprogress')

    @property
    def change_created_at(self):
        posted_date = self.created_at.date()
        today_date = datetime.now().date()
        passed_date = today_date-posted_date
        if passed_date == today_date:
            return "Recently Added"
        else:
            passed_date = str(passed_date).split(', ')[0]
            return passed_date


class StarredJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    starred = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.job.job_title}: {self.user.email}'
