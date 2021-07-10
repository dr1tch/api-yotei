from rest_framework import generics, filters
from rest_framework.views import APIView
from taggit_serializer.serializers import TaggitSerializer
from .models import Service
from .serializers import ServiceSerializer, TagsSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from taggit.models import Tag


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
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly,
                          ServiceWritePermission, IsServiceProvider]
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ['name', 'tags__name']
    filterset_fields = ['category__id', 'wilaya__id']

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticatedOrReadOnly, ServiceWritePermission, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class TagsList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer


class TagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
