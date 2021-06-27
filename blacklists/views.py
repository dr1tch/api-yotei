from .models import Blacklist
from rest_framework import generics
from .serializers import BlacklistSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated

# Create your views here.


class BlacklistList(generics.ListCreateAPIView):
    serializer_class = BlacklistSerializer
    queryset = Blacklist.objects.all()


class BlacklistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlacklistSerializer
    queryset = Blacklist.objects.all()


# class
