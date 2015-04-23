"""
WSGI config for atmtweet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

#PAOLO - Serve per usarlo sotto Apache mod_wsgi
import sys
sys.path.append('/var/www/django/projects/atm-tweet-server')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atmtweet.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
