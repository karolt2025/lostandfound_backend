from django.urls import path
from django.http import HttpResponse

# Test view
def home(request):
    return HttpResponse("🎉 Django server is working!")

urlpatterns = [
    path('', home, name='home'),  # This will be served at /items/ because of project urls.py
]
