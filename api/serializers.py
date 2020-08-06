from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post, Writer

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    write_only_fields = ['password',]

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )

    if self.is_valid():
      user.set_password(validated_data['password'])
      user.save()

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
