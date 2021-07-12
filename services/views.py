from sms import Message
from django.conf import settings
from twilio.rest import Client
import os
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from taggit_serializer.serializers import TaggitSerializer
from .models import Service
from .serializers import ServiceSerializer, TagsSerializer
from rest_framework.permissions import AllowAny, SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from taggit.models import Tag
from sms import send_sms
from rest_framework.response import Response
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse


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


class SendSMS(APIView):
    permission_classes = [AllowAny]

    # def post(self, request):
    #     send_sms(
    #         'Here is the message',
    #         '+213662490933',
    #         ['+213662490933'],
    #         fail_silently=False
    #     )
    #     return Response(status=status.HTTP_200_OK)
    def post(self, request):
        print(request.data.get('message', ''))
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        phone_number = settings.TWILIO_PHONE_NUMBER
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=phone_number,
            body=request.data.get("message"),
            to=request.data.get('to', '')
        )
        print(message.sid)
        return Response('sent!', status=status.HTTP_200_OK)
