from users.models import User
from services.models import Service
from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Appointment(models.Model):
    class Status(models.IntegerChoices):
        APPROUVED = 2
        PENDING = 1
        REJECTED = 0
    base_status = Status.PENDING
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='service_appointment')
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client_appointment')
    day = models.DateField(blank=False)
    start = models.TimeField(blank=False)
    end = models.TimeField(blank=False)
    status = models.IntegerField(
        _("Status"), choices=Status.choices, default=base_status
    )
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'

    def __str__(self):
        return "{} got appointment with {} ".format(self.client.name, self.service.name)
