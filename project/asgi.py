"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django

# 🔧 Inicializar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

# ✅ Ahora que Django está cargado, importa lo demás
from strawberry.asgi import GraphQL
from core.schema import schema

application = GraphQL(schema)