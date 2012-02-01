from django.conf import settings


def facebook(request):
    """
    Adds Facebook-specific context variables to context.
    """
    return {
        'FACEBOOK_APP_ID': getattr(settings, 'FACEBOOK_APP_ID', None),
        'FACEBOOK_SECRET_KEY': getattr(settings, 'FACEBOOK_SECRET_KEY', None),
        'FACEBOOK_PERMS': getattr(settings, 'FACEBOOK_EXTENDED_PERMISSIONS',
            None),
    }
