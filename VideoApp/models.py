import uuid

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#userProfile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=True)

    def __str__(self):  # Corrected method name to '__str__' instead of 'str'
        return self.user.username

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/video/')
    created_at = models.DateTimeField(auto_now_add=True)
    video_link = models.URLField()

    def save(self, *args, **kwargs):
        self.video_link = self.file.url  # Automatically sets video_link to the URL of the uploaded video file
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.description}"



