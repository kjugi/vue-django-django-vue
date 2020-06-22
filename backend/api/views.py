from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Post, Writer
from .serializers import WriterSerializer, PostSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class PostViewSet(viewsets.ModelViewSet):
  """
    API - Posts are visible and editable
  """
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class WriterViewSet(viewsets.ModelViewSet):
  queryset = Writer.objects.all()
  serializer_class = WriterSerializer