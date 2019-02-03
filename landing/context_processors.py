__author__ = 'berluskuni'
from .settings import PORTAL_URL


def portal_url(request):
    return {'PORTAL_URL': PORTAL_URL}

