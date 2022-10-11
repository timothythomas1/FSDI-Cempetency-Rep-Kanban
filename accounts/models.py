from email.policy import default
from time import timezone
from django.db import models
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group, AbstractBaseUser, AbstractUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
        unique=False,
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=255,
        unique=False,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = CustomUserManager()

    def __str__(self):
        return self.username