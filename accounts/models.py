from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    ROLE_CHOICES = [
        ('SUPERADMIN', 'Super Admin'),
        ('HR', 'HR Manager'),
        ('RECRUITER', 'Recruiter'),
        ('MANAGER', 'Department Manager'),
        ('EMPLOYEE', 'Employee'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')

    def __str__(self):
        return self.user.username