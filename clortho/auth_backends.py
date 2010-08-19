from datetime import datetime

from django.contrib.auth.models import User
from django.conf import settings

import facebook
from clortho.models import Facebook

class FacebookBackend:
    
    def authenticate(self, cookies):
        APP_ID = settings.FACEBOOK_APP_ID
        SECRET_KEY = settings.FACEBOOK_SECRET_KEY
        NS = settings.FACEBOOK_USER_NAMESPACE
        try:
            access_token = facebook.get_user_from_cookie(cookies, APP_ID, SECRET_KEY)
            token_not_expired = datetime.fromtimestamp(float(access_token['expires'])) > datetime.now()
            if 'fbs_' + APP_ID in cookies and token_not_expired:
                graph = facebook.GraphAPI(access_token['access_token'])
                user_info = graph.get_object('me')
                try:
                    facebook_data = Facebook.objects.get(uid=user_info['id'])
                    return facebook_data.user
                except Facebook.DoesNotExist:
                    try:
                        email = user_info['email']
                    except:
                        email = user_info['id'] + '@dummyfbemail.com'
                    user = User.objects.create(username=NS + user_info['id'], 
                                               email=email)
                    user.first_name = user_info['first_name']
                    user.last_name = user_info['last_name']
                    user.save()
                    # New users get an unusable password.
                    if settings.FACEBOOK_SET_UNUSABLE_PASSWORD:
                        user.set_unusable_password()
                    facebook_data = Facebook(uid=user_info['id'], 
                                             url=user_info['link'], user=user)
                    facebook_data.save()
                    return user
            else:
                return None
        except:
            return None
            
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None