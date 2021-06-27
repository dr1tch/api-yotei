from django.conf.urls import url
from django.urls import path
from .views import ServiceList, ServiceDetail

urlpatterns = [
    path('<int:pk>/', ServiceDetail.as_view()),
    path('', ServiceList.as_view()),
]
