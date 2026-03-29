from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, blank=True, related_name='joined_projects')

    def __str__(self):
        return self.title


class JoinRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.student} → {self.project} ({self.status})"