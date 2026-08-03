"""
Configuration des URLs du projet mademoiselle_fashion.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boutique.urls')),
]

# Sert les fichiers médias en mode développement uniquement.
# En production, WhiteNoise (statiques) et le serveur web (médias) s'en chargent.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
