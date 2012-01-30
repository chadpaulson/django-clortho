from django.conf.urls.defaults import *

urlpatterns = patterns('clortho',

    url(r'^facebook_login/$', 'views.facebook_login',
        name='clortho_fb_login'),
    url(r'^facebook_login_complete/$', 'views.facebook_login_complete',
        name='clortho_fb_login_complete'),

)
