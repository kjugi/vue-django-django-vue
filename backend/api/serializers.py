from rest_framework import serializers
from .models import Post, Writer

class ShortWriterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Writer
    fields = ['id', 'name', 'email']

class PostSerializer(serializers.ModelSerializer):
    writer = ShortWriterSerializer(read_only=True)
    writer_id = serializers.PrimaryKeyRelatedField(
      source='writer',
      queryset=Writer.objects.all(),
    )
    class Meta:
        model = Post
        fields = ['id', 'title', 'urlSlug', 'content', 'categories', 'featureImage', 'writer_id', 'writer']

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = '__all__'

class SinglePostSerializer(serializers.HyperlinkedModelSerializer):
    writer = WriterSerializer()
    class Meta:
        model = Post
        fields = '__all__'
