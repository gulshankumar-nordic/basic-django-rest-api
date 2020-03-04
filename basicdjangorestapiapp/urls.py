from django.urls import path
from .views import getArticles, getArticleById, getPostById, getPosts, getCommentByPostById, getLatestPosts, PostAPIView, PostDetailsAPIView, GenericAPIView


urlpatterns = [
    path('api/v1/articles/', getArticles),
    path('api/v1/article/<int:pk>/', getArticleById),
    path('api/v1/posts/', getPosts),
    path('api/v1/latest-posts/', getLatestPosts),
    path('api/v1/post/<int:pk>/', getPostById),
    path('api/v1/comments/<int:pk>/', getCommentByPostById),
    path('api/v1/post-list/', PostAPIView.as_view()),
    path('api/v1/post-details/<int:id>/', PostDetailsAPIView.as_view()),
    path('api/v1/generic/post-list/', GenericAPIView.as_view()),
]
