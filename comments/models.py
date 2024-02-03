from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)