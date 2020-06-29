from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from rest_framework import viewsets

from .models import Post, Writer
from .serializers import WriterSerializer, PostSerializer, SinglePostSerializer

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


class WriterViewSet(viewsets.ModelViewSet):
  queryset = Writer.objects.all()
  serializer_class = WriterSerializer
