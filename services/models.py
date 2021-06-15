from categories.models import Category
from wilayas.models import Wilaya
from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from users.models import User
from taggit.managers import TaggableManager


class Service(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner_services')
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1500, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_services')
    is_validated = models.BooleanField(default=False)
    address = models.TextField(_("adresse"), blank=True)
    longtitude = models.CharField(max_length=20, blank=False)
    latitude = models.CharField(max_length=20, blank=False)
    wilaya = models.ForeignKey(
        Wilaya, on_delete=models.CASCADE, related_name='wilaya_service')
    phone_number = models.CharField(max_length=11)
    logo = models.ImageField(blank=True)
    tags = TaggableManager(blank=True)
    deleted = models.BooleanField(default=False)
    visibility = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.name

    def get_user(id):
        return User.objects.get(id=id)