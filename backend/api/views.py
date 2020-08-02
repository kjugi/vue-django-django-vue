from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets

from .models import Post, Writer
from .serializers import WriterSerializer, PostSerializer, SinglePostSerializer, UserSerializer

def indexWelcome(request):
  data = {
      'message': 'Hello from API!',
      'version': 0.1
  }
  return JsonResponse(data)

class PostViewSet(viewsets.ModelViewSet):
  """
    API - Posts are visible and editable
  """
  queryset = Post.objects.all().order_by('id')
  model = Post
  serializer_classes = {
    'list': PostSerializer,
    'retrieve': SinglePostSerializer,
  }
  default_serializer_class = PostSerializer

  def get_serializer_class(self):
    return self.serializer_classes.get(self.action, self.default_serializer_class)

  def get_queryset(self):
    queryset = Post.objects.all().order_by('id')
    singlePost = self.request.query_params.get('urlSlug', None)
    postByWriter = self.request.query_params.get('writer_id', None)
    if singlePost is not None:
      queryset = queryset.filter(urlSlug=singlePost)
    elif postByWriter is not None:
      queryset = queryset.filter(writer_id=postByWriter)
    return queryset

class WriterViewSet(viewsets.ModelViewSet):
  queryset = Writer.objects.all()
  serializer_class = WriterSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('id')
  serializer_class = UserSerializer
