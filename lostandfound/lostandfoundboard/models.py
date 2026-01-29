from django.db import models
from django.contrib.auth import get_user_model

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

    date_created = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        get_user_model(),
        related_name="items",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.status})"
