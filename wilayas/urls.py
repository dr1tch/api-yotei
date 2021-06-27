from django.conf.urls import url
from django.urls import path
from .views import WilayaList

urlpatterns = [
    path('', WilayaList.as_view()),
]
