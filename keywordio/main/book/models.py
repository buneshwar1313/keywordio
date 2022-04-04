from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin

from django.db import models
from django.conf import settings
from django.utils import timezone
User = settings.AUTH_USER_MODEL
# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("User Must have email")
        email = self.normalize_email(email)
        user = self.model(email=email , name = name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email , name , password):
        user = self.create_user(email, name , password)
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self.db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=250 , unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """REtrieve full name of user"""
        return self.name

    def get_short_name(self):
        """retrieve short name of user"""
        return self.name


class Book(models.Model):
    Book_Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Created =models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return str(self.Book_Name)