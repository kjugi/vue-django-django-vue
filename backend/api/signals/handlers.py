from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, created, **kwargs):
  if created:
    group = Group.objects.get(name='standard_user')
    instance.groups.add(group)
