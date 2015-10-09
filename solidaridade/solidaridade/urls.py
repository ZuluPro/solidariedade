"""solidaridade URL Configuration"""
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings as sett


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'showcase.views.showcase', name='showcase'),
    url(r'^history$', 'showcase.views.history', name='history'),
    url(r'^engagement$', 'showcase.views.engagement', name='engagement'),
    url(r'^values$', 'showcase.views.values', name='values'),
    url(r'^contact$', 'contact.views.contact', name='contact'),
    url(r'^donation$', 'donation.views.donation', name='donation'),
    url(r'blog/', include('zinnia.urls', namespace='zinnia')),
)

if sett.DEBUG:
    urlpatterns += static(sett.STATIC_URL, document_root=sett.STATIC_ROOT)
    urlpatterns += static(sett.MEDIA_URL, document_root=sett.MEDIA_ROOT)
