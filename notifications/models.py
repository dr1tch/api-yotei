from django.db import models
from users.models import User
# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_notifications')
    read = models.BooleanField(default=False)
    shown = models.BooleanField(default=False)
    body = models.TextField(_("body"), blank=False, max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
        ordering = ('-created_date',)

    def __str__(self):
        return [self.body, self.user]
