import datetime
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from wilayas.models import Wilaya


class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.IntegerChoices):
        CLIENT = 0
        SERVICE_PROVIDER = 1

    base_role = Roles.CLIENT
    username = models.CharField(unique=True, max_length=50, blank=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1500, blank=True)
    address = models.TextField(_("adresse"), blank=True)
    wilaya = models.ForeignKey(
        Wilaya, on_delete=models.CASCADE, related_name='wilaya_user', null=True)
    phone_number = models.CharField(max_length=11)
    logo = models.ImageField(blank=True)
    date_of_birth = models.DateField(default=datetime.date(1995, 12, 21))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    role = models.IntegerField(
        _("Role"), choices=Roles.choices, default=base_role
    )
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email


class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_validated = models.BooleanField(default=0)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)