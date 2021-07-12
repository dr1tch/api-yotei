from .models import Appointment
from rest_framework import generics, filters
from .serializers import AppointmentSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# TODO: Define permission: blacklisted user can't take oppointments


class AppointmentList(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = ['service__id', 'client__id', 'status', 'confirmed']

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


# class
