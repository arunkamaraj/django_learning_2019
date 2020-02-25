from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager

class UserProfileManager(UserManager):

    def create_user(self, email, name, password):

        # usually serializer will do that validator
        if not email:
            raise ValueError("Enter valid Email ID")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.name

    def get_long_name(self):
        return self.name

class FeedItem(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_on = models.TimeField(auto_now_add=True)


