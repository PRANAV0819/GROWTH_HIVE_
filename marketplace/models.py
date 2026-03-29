from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Item(models.Model):
    # Link the item to the user who is selling it
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marketplace_items')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # e.g., 999.99
    
    # The ImageField handles the file upload. 
    # 'upload_to' tells Django which folder to save these images in.
    image = models.ImageField(upload_to='marketplace_images/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - ₹{self.price}"