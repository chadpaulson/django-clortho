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
from models import ClorthoUser, Keymaster
from settings import FACEBOOK_APP_ID, FACEBOOK_SECRET_KEY


def facebook_login(request):
    """
    Redirects user to Facebook authorization screen.
    """
    if request.GET.get('next'):
        request.session['next_url'] = request.GET.get('next')
    else:
        request.session['next_url'] = getattr(settings,
            'LOGIN_REDIRECT_URL', '/')

    uri = request.build_absolute_uri(reverse('clortho_fb_login_complete'))
    url = 'https://graph.facebook.com/oauth/authorize?' + urlencode({
        'client_id': FACEBOOK_APP_ID,
        'redirect_uri': uri,
        'scope': getattr(settings, 'FACEBOOK_EXTENDED_PERMISSIONS', ''),
    })

    return HttpResponseRedirect(url)


def facebook_login_complete(request):
    """
    Handles Facebook authorization callback.
    """

    if request.GET.get('error'):
        return HttpResponseRedirect(getattr(settings, 'LOGIN_URL', '/'))
    else:
        graph = get_facebook_graph(request)

    if graph:
        me = graph.get_object('me')
        user = authenticate(service='facebook', key=me['id'])
        extended_perms = settings.FACEBOOK_EXTENDED_PERMISSIONS

        if not user:
            try:
                if 'email' in extended_perms.split(','):
                    u = ClorthoUser.objects.get(email=me['email'])
                    Keymaster(user=u, service='facebook', key=me['id']).save()
                    user = authenticate(service='facebook', key=me['id'])
            except:
                user = None

        if not user:
            request.session['clortho_fb_access_token'] = graph.access_token
            url = reverse(getattr(settings, 'CLORTHO_AUTH_REDIRECT', '/'))
            return HttpResponseRedirect(url)

        login(request, user)

        try:
            next_url = request.session['next_url']
            request.session['next_url'] = None
        except:
            next_url = getattr(settings, 'LOGIN_REDIRECT_URL', '/')

        return HttpResponseRedirect(next_url)

    error_url = getattr(settings, 'CLORTHO_AUTH_ERROR', '/')
    return HttpResponse(error_url)
