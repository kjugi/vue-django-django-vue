import re
from django.core.validators import validate_comma_separated_integer_list
from django.core.exceptions import ValidationError
from django.db import models
from jsonfield import JSONField

class Writer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.TextField()
    socialLinks = JSONField(null=True)
    # image = models.ImageField() - pip install Pillow or FilePathField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featureImage = models.CharField(max_length=200) # FilePathField
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    categories = JSONField(null=True)
    areCommentsEnabled = models.BooleanField(default=True)
    urlSlug = models.CharField(max_length=255, blank=True, default='')

    def clean(self):
      withoutSpaces = re.sub(r"[^\w\s]", '', self.title)
      slugFromTitle = re.sub(r"\s+", '-', withoutSpaces).lower()

      if self.urlSlug and Post.objects.exclude(pk=self.pk).filter(urlSlug=self.urlSlug).exists():
        raise ValidationError({
          'urlSlug': 'Post with this slug already exists.'
        })
      elif not self.urlSlug and Post.objects.exclude(pk=self.pk).filter(urlSlug=slugFromTitle).exists():
        raise ValidationError({
          'urlSlug': 'Post with slug like title already exists.'
        })

    def save(self, *args, **kwargs):
      if not self.urlSlug:
        withoutSpaces = re.sub(r"[^\w\s]", '', self.title)
        self.urlSlug = re.sub(r"\s+", '-', withoutSpaces).lower()

      super(Post, self).save(*args, **kwargs)
