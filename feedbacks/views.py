

from .models import Feedback
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FeedbackSerializer
from django_filters.rest_framework import DjangoFilterBackend


# TODO: Define permision: blacklisted user can't take oppointments


class FeedbackList(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = ['service__id', 'client__id', 'type']
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
