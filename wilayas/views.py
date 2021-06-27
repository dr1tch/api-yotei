from rest_framework import generics
from .models import Wilaya
from .serializers import WilayaSerializer
from rest_framework.permissions import AllowAny
# Create your views here.
class WilayaList(generics.ListAPIView):
    permission_classes = [AllowAny,]
    queryset = Wilaya.objects.all()
    serializer_class = WilayaSerializer