from datetime import datetime

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages

import facebook

def on_facebook_authentication(request):
    APP_ID = settings.FACEBOOK_APP_ID
    SECRET_KEY = settings.FACEBOOK_SECRET_KEY
    VIEW = settings.CLORTHO_AUTH_REDIRECT
    access_token = False
    if 'fbs_' + APP_ID in request.COOKIES:
        access_token = facebook.get_user_from_cookie(request.COOKIES, APP_ID, SECRET_KEY)

        if datetime.fromtimestamp(float(access_token['expires'])) > datetime.now():
            user = authenticate(cookies=request.COOKIES)
            if user:
                login(request, user)
                # Pump this to the User for display on the UI.
                messages.info(request, 'You have logged in.')
                return HttpResponseRedirect(reverse(VIEW))
                
        del request.COOKIES['fbs_' + APP_ID]
        
    return HttpResponseRedirect(reverse(VIEW))