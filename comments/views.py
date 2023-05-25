from rest_framework import generics, permissions
from woodshed_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer



