from django.db import models
from django.utils import timezone

# Create your models here.


class Wilaya(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    deleted_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'wilaya'
        verbose_name_plural = 'wilayas'

    def __str__(self):
        return self.name