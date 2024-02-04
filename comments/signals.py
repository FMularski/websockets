from django.db.models.signals import post_save
from django.dispatch import receiver
from comments import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=models.Comment)
def send_comments_via_ws(instance, created, *args, **kwargs):
    group_name = f"user_{instance.user.pk}"
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "send_comments",
        }
    )

