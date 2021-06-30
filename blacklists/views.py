from .models import Blacklist
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import BlacklistSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class BlacklistList(generics.ListCreateAPIView):
    serializer_class = BlacklistSerializer
    queryset = Blacklist.objects.all()


class BlacklistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlacklistSerializer
    queryset = Blacklist.objects.all()


class BlacklistDelete(APIView):
    # serializer_class = BlacklistSerializer

    def post(self, request):
        user = request.data.get('user')
        service = request.data.get('service')
        blacklist = Blacklist.objects.filter(
            service=service, client=user).first()
        blacklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
