from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class ServiceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer