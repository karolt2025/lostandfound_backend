from django.contrib import admin
from django.urls import path, include
# from users.views import CustomAuthToken  # your custom auth token view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('lostandfoundboard/', include('lostandfoundboard.urls')),  # include your app URLs under /items/
    path('users/', include('users.urls')),             # include users app URLs under /users/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)