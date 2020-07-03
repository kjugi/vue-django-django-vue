from rest_framework import serializers
from .models import Post, Writer

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    writer = WriterSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'categories', 'featureImage', 'writer']

class SinglePostSerializer(serializers.HyperlinkedModelSerializer):
    writer = WriterSerializer()
    class Meta:
        model = Post
        fields = '__all__'
