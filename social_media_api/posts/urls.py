from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedListView, like_post, unlike_post
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedListView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', like_post, name='post-like'),
    path('posts/<int:pk>/unlike/', unlike_post, name='post-unlike'),
]
