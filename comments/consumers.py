from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from comments import serializers, models
import json


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_authenticated:
            self.group_name = f"user_{self.user.pk}"
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name,
            )

            await self.accept()
        else:
            await self.close()

    @database_sync_to_async
    def get_comments(self):
        comments = models.Comment.objects.filter(user=self.user)
        serializer = serializers.CommentSerializer(comments, many=True)

        return serializer.data

    async def send_comments(self, event):
        comments_data = await self.get_comments()
        print(comments_data)
        await self.send(text_data=json.dumps(comments_data))

    async def disconnect(self, code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name,
            )

        return await super().disconnect(code)
