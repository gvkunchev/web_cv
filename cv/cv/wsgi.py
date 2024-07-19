"""
WSGI config for cv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

# Include Django's project root in pythonpath to ensure working imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cv.settings')

application = get_wsgi_application()
