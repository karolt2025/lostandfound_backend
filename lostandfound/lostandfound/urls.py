from django.contrib import admin
from django.urls import path, include
# from users.views import CustomAuthToken  # your custom auth token view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('lostandfoundboard/', include('lostandfoundboard.urls')),  # include your app URLs under /items/
    path('users/', include('users.urls')),             # include users app URLs under /users/
]
