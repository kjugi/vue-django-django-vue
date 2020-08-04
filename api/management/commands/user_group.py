import logging
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

PERMISSIONS = ['Can add post', 'Can view post', 'Can add writer', 'Can view writer', 'Can add access token', 'Can view access token', 'Can add refresh token', 'Can view refresh token', 'Can add application', 'Can view application']

class Command(BaseCommand):
    def handle(self, *args, **options):
      new_group, created = Group.objects.get_or_create(name='standard_user')

      for permission in PERMISSIONS:
        try:
          get_permission = Permission.objects.get(name=permission)
        except Permission.DoesNotExist:
          logging.warning("Permission not found with name '{}'.".format(permission))
          continue
        new_group.permissions.add(get_permission)
