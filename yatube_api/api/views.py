from rest_framework import viewsets
from posts.models import Post, Group, Comment, User, Follow
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer, CustomUserSerializer, FollowSerialozer
from .permissions import AuthorOrReadOnly, ReadOnly
from django.shortcuts import get_object_or_404
# from api.pagination import PostPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):      # Если в GET-запросе требуется получить информацию об объекте
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


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerialozer

    def get_folow(self):
        follow_id = self.kwargs.get('follow_id')
        return get_object_or_404(Follow, pk=follow_id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
















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
