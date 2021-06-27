from django.conf.urls import url
from django.urls import path
from .views import AppointmentList, AppointmentDetail

urlpatterns = [
    path('<int:pk>/', AppointmentDetail.as_view()),
    path('', AppointmentList.as_view()),
]
