from channels.generic.websocket import AsyncWebsocketConsumer


class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope.__dict__)
        
        await self.accept()