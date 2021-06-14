from django.urls import include, path
from .views import *

urlpatterns = [
    path('auth/', include('rest_auth.urls')),    
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/users', UserListView.as_view(), name='users'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-details'),
]