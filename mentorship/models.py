from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MentorRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_requests')
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_requests')
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'mentor'] 

    def __str__(self):
        return f"{self.student} → {self.mentor} ({self.status})"