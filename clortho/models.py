from django.db import models
from django.conf import settings

from django.utils.importlib import import_module

try:
    ClorthoUser = models.get_model(*settings.CLORTHO_USER_MODEL.rsplit('.', 1))
except:
    from django.contrib.auth.models import User as ClorthoUser


SERVICES = (
    ('facebook', 'Facebook'),
)


class Keymaster(models.Model):
    """
    Associates social services with your chosen user model.
    """
    user = models.ForeignKey(ClorthoUser, related_name='keymaster')
    service = models.CharField(max_length=20, choices=SERVICES)
    key = models.CharField(max_length=255)

    class Meta:
        unique_together = (('user', 'service'), ('service', 'key'))
        verbose_name = 'Clortho User Association'
        verbose_name_plural = 'Clortho User Associations'

    def __unicode__(self):
        return u'%s\'s %s Service' % (self.user.username, self.service)

    def get_avatar(self, size='square'):
        """
        Returns the URL of the user's avatar.

        Facebook Sizes:
            square  (50x50)
            small   (50xVar)
            large   (200xVar)
        """
        if self.service == 'facebook':
            return 'http://graph.facebook.com/%s/picture?type=%s' % (self.key,
            size)
