# from django.urls import path
# from django.http import HttpResponse
# from .views import ItemListCreateView, ItemDetailView, home

# # Test view
# def home(request):
#     return HttpResponse("🎉 Django server is working!")

# urlpatterns = [
#     path('', home, name='home'),  # This will be served at /items/ because of project urls.py
#     path('lostandfoundboard/lostitems/', ItemListCreateView.as_view(), name='items-list'),
#     path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
# ]


from django.urls import path
from .views import ItemListCreateView, ItemDetailView, home

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemListCreateView.as_view(), name='items-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
