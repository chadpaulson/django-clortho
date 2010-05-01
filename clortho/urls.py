from django.conf.urls.defaults import *

urlpatterns = patterns('clortho', 
	url(r'^on-facebook-authentication/$', 'views.on_facebook_authentication', name='on_facebook_authentication'),
)