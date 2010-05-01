INSTALL:
=======

 1. Install [facebook/python-sdk][2].

 2. Drop 'clortho' into your django project.

 3. Add 'clortho' to INSTALLED_APPS in settings.py

 4. Add 'clortho.auth_backends.FacebookBackend' to AUTHENTICATION_BACKENDS in settings.py.

 5. Add the following entry to your project-level urls.py

    url(r'^clortho/', include('clortho.urls')),


 6. Add the following settings to settings.py


    FACEBOOK_API_KEY = 'value_here' #facebook app api key

    FACEBOOK_SECRET_KEY = 'value_here' #facebook app secret key

    FACEBOOK_APP_ID = 'value_here' #facebook app id

    FACEBOOK_USER_NAMESPACE = 'fb-' #will serve as username prefix

    CLORTHO_AUTH_REDIRECT = 'home' #name of url to redirect to after authentication

 7. Follow the included file `example_template.txt`.  Don't forget to set the javascript variable FB_APP_ID, as it should match the value of FACEBOOK_APP_ID you filled out earlier in settings.py.  Future versions of django-clortho will contain a more simple and clean way of integrating the javascript and markup necessary.  Please consult the [Facebook Developer documentation][1] for help on specifics.

TODO:
=====

  - Add template tags for social widgets and auth.
  - Add convenience methods to model for easy API lookups.
  - Add methods to allow existing users to connect via FB.

Motivation
========

This project came to be while I started rewriting my 14 year old Ghostbusters fan site in Python.  I wanted a simple pluggable app to tie into the latest Facebook and Twitter APIs and authentication schemes.  Named after Vinz Clortho, keymaster of Gozer, `django-clortho` will eventually provide OAuth 2.0-based authentication backends to Facebook Graph API and Twitter @Anywhere.


  [1]: http://developers.facebook.com
  [2]: http://github.com/facebook/python-sdk
