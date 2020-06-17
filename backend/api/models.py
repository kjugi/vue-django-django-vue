
from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featureImage = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    bio = models.TextField()

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'writer']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
