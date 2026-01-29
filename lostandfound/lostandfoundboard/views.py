from rest_framework import generics, permissions
# from django.http import Http404
from django.http import HttpResponse
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated


def home(request):
    return HttpResponse("🎉 Django server is working!")

# class ItemListCreateView(generics.ListCreateAPIView):
#     serializer_class = ItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Item.objects.all()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():
#             print("❌ SERIALIZER ERRORS:", serializer.errors)  # 👈 THIS
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
