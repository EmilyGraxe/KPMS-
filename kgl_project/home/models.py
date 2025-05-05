from django.db import models
from django.contrib.auth.models import User  # Import User model for user authentication
from django.contrib.auth.models import AbstractUser  # Import AbstractUser for custom user model
from django.db import models
import re
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password,role, branch):
        if not user_id or not password:
            raise ValueError('Users must have a user id')
        user = self.model(user_id=user_id, role=role, branch=branch)
        user.set_password(password)  # hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id,role, password,branch):
        user = self.create_user(user_id=user_id, password=password,role='manager', branch=branch)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):#permissionMixin is a class that provides default permissions
    branch = models.CharField(max_length=100, null=True, blank=True,choices=(('Main Branch', 'Main Branch'), ('Branch 1', 'Branch 1'), ('Branch 2', 'Branch 2')))
    user_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=(
        ('manager', 'Manager'),
        ('attendant', 'Attendant'),
        ('director', 'Director'),
    
    ))
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)


    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['password', 'role','branch']  # Specify any additional fields required for user creation

    objects = CustomUserManager()

    def __str__(self):
        return self.user_id
    #permissions
    def has_perm(self, perm, obj=None):
        return True  # All users have all permissions

    def has_module_perms(self, app_label):
        return True
    
class TrustedCustomer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    nin = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey('home.CustomUser', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.nin})'

   