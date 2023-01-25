"""
ASGI config for inmansdj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

"""
ASGI config for inmansdj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# from .wsgi import *  # add this line to top of your code
import django
django.setup()
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import get_default_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


django_asgi_app = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmansdj.settings')

from api.consumers import ApiConsumer
from django.urls import re_path

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
    URLRouter([        
        re_path(r'ws/messages/(?P<room_name>\w+)/$', ApiConsumer.as_asgi()),  # (?P<room_name>\w+)/$

    ])
    )
}) 
