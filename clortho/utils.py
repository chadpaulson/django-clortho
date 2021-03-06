import facebook
from django.conf import settings

APP_ID = settings.FACEBOOK_APP_ID
SECRET_KEY = settings.FACEBOOK_SECRET_KEY
NS = settings.FACEBOOK_USER_NAMESPACE

def get_graph(request):
    """
    Shortcut for instantiating a facebook.GraphAPI object.
    
    Returns a complete facebook.GraphAPI object for querying.
    Returns None if Facebook cookie credentials can't be found.
    """
    user = facebook.get_user_from_cookie(request.COOKIES, 
                                         APP_ID, 
                                         SECRET_KEY)
    if user:
        return facebook.GraphAPI(user["access_token"])
    else:
        return None