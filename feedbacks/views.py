

from .models import Feedback
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FeedbackSerializer

# TODO: Define permision: blacklisted user can't take oppointments


class FeedbackList(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
