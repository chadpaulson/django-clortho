from django.contrib.auth.models import User
from django.db import models

class Facebook(models.Model):
    """
    Facebook profile model for a User. Stores a few important details about
    their Facebook account, and has some convenience methods.
    """
    user = models.ForeignKey(User, related_name='facebook')
    uid = models.CharField(max_length=20, unique=True)
    url = models.URLField(blank=True, null=True)
    
    def get_picture_url(self, size="small"):
        """
        Returns the URL for this user's profile picture.
        
        square (50x50), small (50xVar), large (200xVar)
        """
        return "http://graph.facebook.com/%s/picture?type=%s" % (self.uid, 
                                                                 size)
    
    class Meta:
        verbose_name = "Facebook User"
        verbose_name_plural = "Facebook Users"
    
    def __unicode__(self):
        return u'%s %s\'s Facebook Profile' % (self.user.first_name, 
                                               self.user.last_name)