from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import AllowAny
# Create your views here.
class CategoryList(generics.ListAPIView):
    permission_classes = [AllowAny,]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer