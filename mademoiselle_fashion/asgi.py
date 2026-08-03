"""
Configuration ASGI pour le projet mademoiselle_fashion.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mademoiselle_fashion.settings')

application = get_asgi_application()
