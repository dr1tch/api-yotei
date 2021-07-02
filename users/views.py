from rest_framework import viewsets, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout
from rest_framework import generics, filters
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
import json
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import (
    UserSerializer,
    RegisterSerializer,
    PasswordChangeSerializer,
)

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile


class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)


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


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ['name', 'username', 'email', 'phone_number', 'role']
    filterset_fields = ['wilaya__id']
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer


class GetUserByKey(generics.RetrieveAPIView):
    def post(self, request, **kwargs):
        print(request.data['key'])
        # try:
        user_id = Token.objects.get(key=request.data['key']).user_id
        # wilaya = Wilaya.objects.get()
        # user = get_object_or_404(User, id=user_id)
        # user.logo = json.dumps(str(user.logo))
        # result = JsonResponse(  model_to_dict(user) )
        # # result = json.dumps(user, cls=ExtendedEncoder)
        # response = {
        #     'success': True,
        #     'status_code': status.HTTP_200_OK,
        #     'message': 'Successfully fetched users',
        #     # 'users': {
        #     #     'id': user.id,
        #     #     'name': user.name,
        #     #     'email': user.email,
        #     #     'username': user.username,
        #     #     'description': user.description,
        #     #     'role': user.role,
        #     #     'wilaya': {
        #     #         'id': user.wilaya.id,
        #     #         "name": user.wilaya.name,
        #     #     },

        #     #     'address': user.address,
        #     #     'phone_number': user.phone_number,
        #     #     # 'logo': user.logo,
        #     #     'created_date': user.created_date,
        #     #     'token': request.data['key']
        #     # }

        # }
        return Response(user_id, status=status.HTTP_200_OK)
        # except Token.DoesNotExist:
        #     return Response('User not found', status=status.HTTP_404_NOT_FOUND)
