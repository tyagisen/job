from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


SUPER_ADMIN=1
ADMIN=2
EMPLOYEER=3
EMPLOYEE=4
role_choices = (
    (SUPER_ADMIN,"Super Admin"),
    (ADMIN, "Admin"),
    (EMPLOYEER, "Employeer"),
    (EMPLOYEE, "Employee")
)
class Role(models.Model):
    
    id = models.PositiveSmallIntegerField(choices=role_choices, primary_key=True)
    def __str__(self):
        return self.get_id_display()

    def role_dict(self):
        return {role[0]: role[1] for role in self.role_choices}



class User(AbstractUser):
    role = models.ManyToManyField(Role)
    email =models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=False, max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    # def get_roles(self):
    #     all_roles = self.roles.all()
    #     if not all_roles:
    #         return None
    #     user_roles = []
    #     for roles in all_roles:
    #         user_roles.extend(
    #             role_value
    #             for role_id, role_value in Role.role_choices
    #             if roles.id == role_id
    #         )
    #     return user_roles

    # def check_role(self, roles):
    #     return roles in self.roles.all().values_list("id", flat=True)


    @property
    def is_admin(self):
        return self.role==ADMIN

    @property
    def is_employeer(self):
        return self.role==EMPLOYEER


    @property
    def is_employee(self):
        return self.role==EMPLOYEE