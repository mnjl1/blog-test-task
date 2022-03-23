from urllib import request
from rest_framework import generics
from rest_framework.response import Response
from api import serializers
from .models import Post
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = (serializers.PostSerializer(posts, many=True))
    response = [[serializer.data], ]
    return Response(response)

@api_view(['GET'])
def get_post_by_id(request, pk):
    post = Post.objects.get(id=pk)
    serializer = serializers.PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_post(request):
    """
    Creates new blog record
    """
    data = request.data
    title = data['title']
    link = data['link']
    blog = Post.objects.create(
        owner=request.user,
        title=title,
        link=link
    )
    serializer = serializers.PostSerializer(blog, many=False)
    return Response(serializer.data)






# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
