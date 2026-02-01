from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Item
from .serializers import ItemSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


def home(request):
    return HttpResponse("🎉 Django server is working!")


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all().order_by("-date_created")
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Optional filter by status:
        /lostandfoundboard/items/?status=lost
        /lostandfoundboard/items/?status=found
        """
        queryset = super().get_queryset()
        status_param = self.request.query_params.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        item_id = self.request.query_params.get("item")
        other_user_id = self.request.query_params.get("user")

        # ✅ Base queryset: ALL messages involving the user
        queryset = Message.objects.filter(Q(sender=user) | Q(receiver=user))

        # ✅ Conversation-specific filter (used by chat view)
        if item_id and other_user_id:
            queryset = queryset.filter(item_id=item_id).filter(
                Q(sender=user, receiver_id=other_user_id)
                | Q(sender_id=other_user_id, receiver=user)
            )

        # ✅ Newest last (better for chat UI)
        return queryset.order_by("created_at")

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


# class MessageViewSet(ModelViewSet):
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Message.objects.filter(
#             receiver=user
#         ).order_by("-created_at")

#     def perform_create(self, serializer):
#         serializer.save(sender=self.request.user)

#     def create(self, request, *args, **kwargs):
#         print("📨 Incoming message data:", request.data)
#         return super().create(request, *args, **kwargs)


# class MessageViewSet(ModelViewSet):
#     serializer_class = MessageSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user

#         item_id = self.request.query_params.get("item")
#         other_user_id = self.request.query_params.get("user")

#         queryset = Message.objects.filter(Q(sender=user) | Q(receiver=user))

#         if item_id and other_user_id:
#             queryset = queryset.filter(item_id=item_id).filter(
#                 Q(sender=user, receiver_id=other_user_id)
#                 | Q(sender_id=other_user_id, receiver=user)
#             )

#         return queryset.order_by("created_at")

#     def perform_create(self, serializer):
#         serializer.save(sender=self.request.user)

#     def create(self, request, *args, **kwargs):
#         print("📨 Incoming message data:", request.data)
#         return super().create(request, *args, **kwargs)
