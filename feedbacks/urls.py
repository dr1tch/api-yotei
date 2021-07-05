

from django.conf.urls import url
from django.urls import path
from .views import FeedbackList, FeedbackDetail

urlpatterns = [
    path('<int:pk>/', FeedbackDetail.as_view()),
    path('', FeedbackList.as_view()),
]
