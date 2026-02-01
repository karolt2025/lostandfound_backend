from rest_framework import generics
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Item
from .models import Message

User = get_user_model()  # 👈 Use the custom user model


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Item
        fields = [
            "id",
            "title",
            "description",
            "status",
            "location",
            "contact_email",
            "image",
            "date_created",
            "owner",
        ]


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source="sender.username", read_only=True)
    receiver_username = serializers.CharField(
        source="receiver.username", read_only=True
    )

    sender_email = serializers.EmailField(source="sender.email", read_only=True)
    receiver_email = serializers.EmailField(source="receiver.email", read_only=True)

    # ✅ ADD THIS LINE
    item_title = serializers.CharField(source="item.title", read_only=True)

    class Meta:
        model = Message
        fields = [
            "id",
            "sender",
            "receiver",
            "sender_username",
            "receiver_username",
            "sender_email",
            "receiver_email",
            "item",
            "item_title",  # ✅ already correctly listed
            "content",
            "created_at",
            "is_read",
        ]
        read_only_fields = ["sender"]


# class MessageSerializer(serializers.ModelSerializer):
#     sender_username = serializers.ReadOnlyField(source="sender.username")

#     class Meta:
#         model = Message
#         fields = "__all__"
#         read_only_fields = ("sender",)
