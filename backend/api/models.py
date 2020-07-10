from django.core.validators import validate_comma_separated_integer_list
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
    urlSlug = models.CharField(max_length=255, null=True)
