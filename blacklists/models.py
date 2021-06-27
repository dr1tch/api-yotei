from django.db import models
from django.utils import timezone
from services.models import Service
from users.models import User
# Create your models here.


class Blacklist(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_blacklist")
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_blacklist")
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'blacklist'
        verbose_name_plural = 'blacklists'

    def __str__(self):
        return self.service.name
