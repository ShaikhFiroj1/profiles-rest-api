from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """helps django work with our custom user model"""

    def create_user(self, email, name, password=None):
        """create a new user profile object"""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and save new superuser with given detail"""

        user = self.create_superuser(email, name, password)

        user.is_superuser = True
        user.is_staff = True 


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """represent "user profiles" inside our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDs = ['name']

    def get_full_name(self):
        """used to get users full name"""

        return self.name

    def get_short_name(self):
        """used to get users short name"""

        return self.name

    def __str__(self):
        """Djang uses this to convert objects into the strings"""

        self.email