# users/urls.py
from django.urls import path
from .views import RegisterUserView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]
