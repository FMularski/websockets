from django.urls import path
from comments import consumers

websocket_urlpatterns = [
    path('ws/comments/', consumers.CommentConsumer.as_asgi()),
]
