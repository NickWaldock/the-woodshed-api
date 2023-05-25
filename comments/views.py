from rest_framework import generics, permissions
from woodshed_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    query_set = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)