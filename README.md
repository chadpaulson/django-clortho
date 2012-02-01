[![](http://farm5.static.flickr.com/4012/4567211957_8100b745d3_o.jpg)](http://farm5.static.flickr.com/4012/4567211957_8100b745d3_o.jpg)

INSTALL:
--------

 1. `python setup.py install` or [add][3] the repository to your pip requirements file.

 2. Install [facebook/python-sdk][2].

 3. Add `'clortho'` to INSTALLED_APPS in settings.py.

 4. Add `'clortho.auth_backends.ClorthoBackend'` to AUTHENTICATION_BACKENDS in 
    settings.py.

 5. Add the following entry to your project-level urls.py.

    `url(r'^clortho/', include('clortho.urls')),`

 6. Add the following settings to settings.py.

        # Facebook app secret key.
        FACEBOOK_SECRET_KEY = 'value_here'
        # Facebook app id.
        FACEBOOK_APP_ID = 'value_here'
        # Will serve as username prefix.
        FACEBOOK_USER_NAMESPACE = 'fb-'
        # Name of url to redirect to after authentication. 
        CLORTHO_AUTH_REDIRECT = 'home' 
        # Extended Permissions
        FACEBOOK_EXTENDED_PERMISSIONS = ''
  
 7. Optionally, add 'clortho.context_processors.facebook' to your
    TEMPLATE_CONTEXT_PROCESSORS.

 8. Sync your database.

        python manage.py syncdb

OPTIONAL SETTINGS:
------------------

`CLORTHO_ASSOCIATE_BY_EMAIL` Boolean

        This setting tells clortho if it should automatically associate an
        existing application user when the email address is available in the
        social context.


TODO:
-----

  - Add other social backends (Twitter, Google Oauth2, Yahoo OpenID, etc.)
  - Add convenience methods to model for easy API lookups.
  - Add methods to allow existing users to connect with various services.

Motivation
----------

This project came to be while I started rewriting my 14 year old Ghostbusters 
fan site in Python.  I wanted a simple pluggable app to tie into the latest 
Facebook and Twitter APIs and authentication schemes.  Named after 
Vinz Clortho, Keymaster of Gozer, `django-clortho` will eventually provide 
OAuth 2.0-based authentication backends to Facebook Graph API and Twitter Oauth, among others.

  [1]: http://developers.facebook.com
  [2]: http://github.com/facebook/python-sdk
  [3]: http://www.pip-installer.org/en/latest/requirement-format.html#git