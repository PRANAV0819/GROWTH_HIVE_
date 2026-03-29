from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    STATUS_CHOICES = (
        ('lost', 'Lost'),
        ('found', 'Found'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lostfound_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"