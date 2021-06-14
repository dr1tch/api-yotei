from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout
from rest_framework import generics
from .models import User

from .serializers import (
    UserSerializer,
    RegisterSerializer,
    PasswordChangeSerializer,
)

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)

class PasswordChangeView(APIView):
    def post(self, request):
        serializer_class = PasswordChangeSerializer
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get(self, request):
        queryset = User.objects.filter(is_superuser=False)
        serializer = self.serializer_class(queryset, many=True)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully fetched users',
            'users': serializer.data

        }
        return Response(response, status=status.HTTP_200_OK)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

