from rest_framework import generics

from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAdminUser]
    #authentication_classes = [SessionAuthentication]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer