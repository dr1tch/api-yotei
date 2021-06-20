from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated

class ServiceWritePermission(BasePermission):
    message = 'Editing Service is restricted to the Service Provider only'

    def has_object_permission(self, request, view, obj):
        print(request)
        if request.method in SAFE_METHODS:
            return True
        else:
            print('lksqkljlqsl', obj.owner == request.user)
            return obj.owner == request.user


class IsServiceProvider(BasePermission):
    message = 'Must be a Service Provider! Build a company bitch!!!'

    # def has_permission(self, request, view):
    #     return super().has_permission(request, view)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        print('kqjlskjlqkjklj', request.user.role)
        return request.user.role


class ServiceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ServiceWritePermission, IsServiceProvider]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ServiceWritePermission, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer