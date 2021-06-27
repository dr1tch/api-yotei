from django.conf.urls import url
from django.urls import path
from .views import CategoryList

urlpatterns = [
    path('', CategoryList.as_view()),
]
