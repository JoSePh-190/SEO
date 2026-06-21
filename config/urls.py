from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap

from core.sitemaps import (
    StaticViewSitemap,
    BlogSitemap
)

sitemaps = {
    'static': StaticViewSitemap,
    'blogs': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
