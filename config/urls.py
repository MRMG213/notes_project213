from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("notes.urls")),
]

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
