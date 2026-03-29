from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
       ('student', 'Student'),
       ('alumni', 'Alumni'),
       ('teacher', 'Teacher'),
       ('admin', 'Admin'),
)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)

    # 🔥 ADD IMAGE HERE (IMPORTANT)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return self.user.username