from users.models import User
from services.models import Service
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from django.db import models

# Create your models here.


class Feedback(models.Model):

    # 0 : CLIENT ===> SERVICE
    # 1 : SERVICE ===> CLIENT
    class Types(models.IntegerChoices):
        CLIENT = 0
        SERVICE = 1

    base_type = Types.CLIENT
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client_feedback')
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='service_feedback')
    type = models.IntegerField(
        _("Type"), choices=Types.choices, default=base_type
    )
    rating = models.FloatField(blank=False)
    body = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
        ordering = ('-created_date',)

    def __str__(self):
        return str(self.body)
