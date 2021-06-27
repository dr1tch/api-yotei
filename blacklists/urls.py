from django.conf.urls import url
from django.urls import path
from .views import BlacklistList, BlacklistDetail

urlpatterns = [
    path('<int:pk>/', BlacklistDetail.as_view()),
    path('', BlacklistList.as_view()),
]
