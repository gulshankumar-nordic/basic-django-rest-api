from django.urls import path
from .views import getAllArticle, getArticleById

urlpatterns = [
    path('api/v1/articles/', getAllArticle),
    path('api/v1/article/<int:pk>/', getArticleById),
]
