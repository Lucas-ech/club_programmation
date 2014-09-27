from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'list', name='projects_list'),
    url(r'^voir/(?P<slug>[0-9a-zA-Z-]+)$', 'view', name='projects_view'),
    url(r'^editer/(?P<slug>[0-9a-zA-Z-]+)$', 'edit', name='projects_edit'),
    url(r'^creer/$', 'create', name='projects_edit'),
    url(r'^sauvegarder_commentaire/(?P<slug>[0-9a-zA-Z-]+)$', 'save_comment', name='projects_savecomment'),
)
