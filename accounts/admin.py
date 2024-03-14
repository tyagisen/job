from django.contrib import admin
from .models import User, Role
# Register your models here.
admin.site.register(User)
admin.site.register(Role)
# class UserAdmin(admin.ModelAdmin):
    # list_display = ['username','email']