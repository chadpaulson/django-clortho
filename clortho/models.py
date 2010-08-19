from django.contrib.auth.models import User
from django.db import models

class Facebook(models.Model):

	user = models.ForeignKey(User, related_name='facebook')
	uid = models.CharField(max_length=20, unique=True)
	url = models.URLField(blank=True, null=True)
	
	def __unicode__(self):
		return u'%s %s\'s Facebook Profile' % (self.user.first_name, self.user.last_name)