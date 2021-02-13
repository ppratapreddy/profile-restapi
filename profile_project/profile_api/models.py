from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ This is BaseUserManger """
    def create_user(self,email,name,password=None):
        """ this will create the user """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email= self.normalize_email(email),name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,email,name,password):
        """ Creates and saves a superuser with the given email and password  """
        user = self.create_user(email,password,password)
        user.is_admin = True
        user.is_staff = True
        user.save(self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ this is to create  customize user model  """
    email = models.EmailField(max_length=200,unique=True)
    name = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']

    def __str__(self):
        """ this will return name as an object """
        return self.name
    
    def get_full_name(self):
        """ This will get the full name"""
        return self.name

    def get_short_name(self):
        """ this will get the short name"""
        return self.name
    

