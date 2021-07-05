

from django.conf.urls import url
from django.urls import path
from .views import NotificationList, NotificationDetail

urlpatterns = [
    path('<int:pk>/', NotificationDetail.as_view()),
    path('', NotificationList.as_view()),
]
