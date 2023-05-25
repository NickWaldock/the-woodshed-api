from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from woodshed_api.permissions import IsOwnerOrReadOnly


class PostList(APIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostDetail(APIView):
    """
    Displays the details of a single post instance, allows post owner to
    edit, and delete
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):  # Check to see if a post exists
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):  # Retrieve a post by ID
        post = self.get_object(pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):  # Updates a post instance
        post = self.get_object(pk)
        serializer = PostSerializer(
            post,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Deletes a post instance
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)