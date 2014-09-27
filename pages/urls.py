from django.conf.urls import patterns, url

urlpatterns = patterns('pages.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^presentation/$', 'presentation', name='presentation'),
    url(r'^editer/(?P<name>[0-9a-zA-Z-]+)$', 'edit', name='pages_edit'),
)
