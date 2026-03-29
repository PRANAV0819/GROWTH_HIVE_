from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marketplace_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
