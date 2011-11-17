from datetime import datetime
from urllib import urlencode


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages


import facebook
from utils import get_facebook_graph
from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY, FACEBOOK_USER_NAMESPACE



def facebook_login(request):
    """
    Redirects user to Facebook authorization screen.
    """
    if request.GET.get('next'):
        request.session['facebook_login_next'] = request.GET.get('next')
        
    url = 'https://graph.facebook.com/oauth/authorize?' + urlencode({
        'client_id': FACEBOOK_APP_ID,
        'redirect_uri': request.build_absolute_uri(reverse('clortho_facebook_login_complete')),
        'scope': 'email', # TODO: make extended permissions an app setting
    })
    
    return HttpResponseRedirect(url)


def facebook_login_complete(request):
    """
    Handles Facebook authorization callback.
    """
    graph = get_facebook_graph(request)
    if graph:
        me = graph.get_object('me')
        user = authenticate(service='facebook', key=me['id'])

        if not user:
            
            # TODO handle auto-association by email
            
            return HttpResponseRedirect(reverse(settings.CLORTHO_ASSOCIATE_URL))

        login(request,user)    
    
        next_url = request.session.get('facebook_login_next', settings.CLORTHO_AUTH_REDIRECT)
        return HttpResponseRedirect(reverse(next_url))
    
    return HttpResponse(reverse(settings.CLORTHO_AUTH_ERROR))
