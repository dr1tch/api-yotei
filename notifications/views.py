

from .models import Notification
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NotificationSerializer

# TODO: Define permision: blacklisted user can't take oppointments


class NotificationList(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
