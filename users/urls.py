from django.conf.urls import patterns, url, include

extra_patterns = patterns('',
    url(r'^configuration/$',
        'django.contrib.auth.views.password_change',
        {'template_name': 'users/configuration.html'}, name='users_configuration'),
    url(r'^configuration/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'users/configuration_done.html'}, name='password_change_done'),
)

urlpatterns = patterns('users.views',
    url(r'^connexion/$', 'login', name='users_login'),
    url(r'^deconnexion/$', 'logout', name='users_logout'),
    url(r'^mon-compte/$', 'myaccount', name='users_myaccount'),
    url(r'^getUsersByUsername/$', 'getUsersByUsername'),
    url(r'^', include(extra_patterns)),
)
