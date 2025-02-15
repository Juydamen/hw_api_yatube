from rest_framework import viewsets
from posts.models import Post, Group, Comment, User, Follow
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer, CustomUserSerializer, FollowSerialozer, PostCommSerializer
from .permissions import AuthorOrReadOnly, ReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = None

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def get_post(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_quetyset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = None


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerialozer
    pagination_class = None

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCommViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCommSerializer
    pagination_class = None













############################################################
# from rest_framework import viewsets

# from posts.models import Cat, Owner

# from .serializers import CatSerializer, OwnerSerializer


# class CatViewSet(viewsets.ModelViewSet):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class OwnerViewSet(viewsets.ModelViewSet):
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer
