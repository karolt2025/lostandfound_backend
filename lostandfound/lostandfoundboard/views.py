from rest_framework import generics, permissions
# from django.http import Http404
from django.http import HttpResponse
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly

def home(request):
    return HttpResponse("🎉 Django server is working!")

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by("-date_created")
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optional filter by status:
        /api/items/?status=lost
        /api/items/?status=found
        """
        queryset = super().get_queryset()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class ItemDetailView(generics.RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
