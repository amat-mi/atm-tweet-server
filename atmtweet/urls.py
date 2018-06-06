# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path as url, include
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # Examples:
    # url(r'^$', 'atmtweet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^tweet/', include('tweet.urls')),

    # Questa è l'URL per la UI Client (in remoto gestita direttamente dal Web Server)
    url(r'^client/', RedirectView.as_view(url='/static/index.html', permanent=False), name="client"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)