from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RSVP(models.Model):
    STATUS_CHOICES = [
        ('Going', 'Going'),
        ('Maybe', 'Maybe'),
        ('Not Going', 'Not Going'),
    ]
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
