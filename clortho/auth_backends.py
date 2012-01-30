from datetime import datetime


from django.conf import settings
from django.contrib.auth.backends import ModelBackend


from clortho.models import Keymaster, ClorthoUser


class ClorthoBackend(ModelBackend):

    def authenticate(self, service, key):
        try:
            return Keymaster.objects.get(service=service, key=key).user
        except Keymaster.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return ClorthoUser.objects.get(pk=user_id)
        except ClorthoUser.DoesNotExist:
            return None
