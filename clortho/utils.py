import facebook
import urllib2
from urllib import urlencode
from urlparse import urlparse
from datetime import datetime


from django.conf import settings
from django.core.urlresolvers import reverse


from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY


def auth_facebook(request):
    """
    Parses initial auth response and returns Facebook Graph Object

    Returns a facebook authorization token for accessing the GraphAPI.
    Returns None if authorization has failed.
    """

    try:
        fbuser = facebook.get_user_from_cookie(request.COOKIES,
            FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY)
        fb_expiry = datetime.fromtimestamp(float(fbuser.get('expires')))

        if fbuser.get('access_token') and fb_expiry > datetime.now():
            return facebook.GraphAPI(fbuser['access_token'])
        else:
            raise Exception
    except:
        uri = request.build_absolute_uri(reverse('clortho_fb_login_complete'))
        url = 'https://graph.facebook.com/oauth/access_token?' + urlencode({
            'client_id': FACEBOOK_APP_ID,
            'client_secret': FACEBOOK_SECRET_KEY,
            'redirect_uri': uri,
            'code': request.GET.get('code'),
        })

        response = urlparse(urllib2.urlopen(url).read())
        params = dict([part.split('=') for part in response[2].split('&')])

        if not params.get('access_token'):
            return None
        else:
            return facebook.GraphAPI(params.get('access_token'))


def get_facebook_graph(request):
    """
    Retrieves Facebook graph object for a given auth token.
    """

    try:
        token = request.session['clortho_fb_access_token']
    except:
        token = None

    try:
        graph = facebook.GraphAPI(token)
        return graph
    except:
        raise
