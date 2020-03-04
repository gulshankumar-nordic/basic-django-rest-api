from rest_framework import serializers
from .models import Articles, Post, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['id', 'title', 'author']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title',  'author', 'body', 'status', 'updated']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Comment
        fields = ['id', 'post', 'name', 'email',
                  'body', 'created', 'updated', 'active']
