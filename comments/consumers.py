from channels.generic.websocket import AsyncWebsocketConsumer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, code):
        return await super().disconnect(code)