# Generated by Django 4.2.10 on 2024-02-17 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0004_alter_job_job_image_one_alter_job_job_image_three_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='post_code',
            field=models.CharField(max_length=50),
        ),
    ]
