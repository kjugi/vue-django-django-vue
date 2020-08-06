from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Writer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']

  def save(self, *args, **kwargs):
    user = super(UserSerializer, self).save(*args, **kwargs)
    user.set_password(make_password(user.password))
    if self.is_valid():
      user.save(update_fields=['password'])
    return user

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

    def validate(self, attrs):
      instance = Post(**attrs)
      instance.clean()
      return attrs

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
