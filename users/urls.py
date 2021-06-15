from django.urls import include, path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('auth/', include('rest_auth.urls')),    
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/users', UserListView.as_view(), name='users'),
    path('auth/users/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('auth/users/get', GetUserByKey.as_view(), name='get-user-after-auth'),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
]