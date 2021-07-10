from django.conf.urls import url
from django.urls import path
from .views import ServiceList, ServiceDetail, TagsDetail, TagsList

urlpatterns = [
    path('<int:pk>/', ServiceDetail.as_view()),
    path('', ServiceList.as_view()),
    path('tags/', TagsList.as_view()),
    path('tags/<int:pk>/', TagsDetail.as_view())
]
