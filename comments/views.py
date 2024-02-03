from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from comments import models, serializers, filters


class CommentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filterset_class = filters.CommentFilter

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
