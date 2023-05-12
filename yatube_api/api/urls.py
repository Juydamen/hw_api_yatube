from django.urls import path, include
from api.views import PostViewSet, GroupViewSet, CommentViewSet, UserViewSet, FollowViewSet, PostCommViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet,)
router.register(r'postcomm', PostCommViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

























##############################################################
# from rest_framework.routers import SimpleRouter, DefaultRouter
# from django.urls import include, path
# from api.views import CatViewSet, OwnerViewSet

# # router = SimpleRouter()
# router = DefaultRouter()
# router.register('cats', CatViewSet)
# router.register('owners', OwnerViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
