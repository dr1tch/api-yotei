from .models import Feedback
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FeedbackSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated

# Create your views here.
# TODO: Define permision: blacklisted user can't take oppointments


class FeedbackList(generics.ListCreateAPIView):
    # filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    # search_fields = ['client__client_feedback',
    #                  'service__service__feedback']
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


# class
