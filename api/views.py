from rest_framework import generics
from rest_framework.response import Response
from api import serializers
from .models import Post, Comment
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_posts(request):
    """
    Display all posts
    """
    posts = Post.objects.all()
    serializer = serializers.PostSerializer(posts, many=True)
    response = [
        [serializer.data],
    ]
    return Response(response)


@api_view(["GET"])
def get_post_by_id(request, pk):
    """
    Get post by id
    """
    post = Post.objects.get(id=pk)
    serializer = serializers.PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create_post(request):
    """
    Creates new post record
    """
    data = request.data
    title = data["title"]
    link = data["link"]
    blog = Post.objects.create(owner=request.user, title=title, link=link)
    serializer = serializers.PostSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def update_post(request, pk):
    """
    Update post record
    """
    data = request.data
    post = Post.objects.get(id=pk)
    serializer = serializers.PostSerializer(instance=post, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_post(request, pk):
    """
    Delete post
    """
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Post was deleted")


@api_view(["PUT"])
def upvote_post(request, pk):
    """
    Upvote post
    """
    post = Post.objects.get(id=pk)
    post.likes_count = post.likes_count + 1
    post.save()
    return Response("Post upvoted")


class CommentList(generics.ListCreateAPIView):
    """
    Create commet
    """

    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
