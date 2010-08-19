from django.conf import settings

def facebook_api_values(request):
    """
    Returns common context stuff for use in HTML templates.
    """
    return {
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID,  
    }