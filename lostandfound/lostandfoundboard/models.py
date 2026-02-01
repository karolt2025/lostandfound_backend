from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Item(models.Model):
    STATUS_CHOICES = [
        ("lost", "Lost"),
        ("found", "Found"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    location = models.CharField(max_length=200)

    contact_email = models.EmailField()

    image = models.ImageField(upload_to="item_images/", blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        get_user_model(),
        related_name="items",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.status})"

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="received_messages",
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        "Item",
        related_name="messages",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"