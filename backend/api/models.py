from django.core.validators import validate_comma_separated_integer_list
from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.TextField()
    socialLinks = models.CharField(max_length=255, validators=[validate_comma_separated_integer_list])
    # image = models.ImageField() - pip install Pillow or FilePathField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featureImage = models.CharField(max_length=200) # FilePathField
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    categories = models.CharField(max_length=255, validators=[validate_comma_separated_integer_list])
    areCommentsEnabled = models.BooleanField(default=True)
    # urlSlug = models. - example of custom url slug
