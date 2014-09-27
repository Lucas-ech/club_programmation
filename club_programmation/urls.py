from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'club_programmation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^utilisateurs/', include('users.urls')),
    url(r'^projets/', include('projects.urls')),
    url(r'^', include('pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


def pageError(request, code):
    response = render_to_response(str(code) + '.html', {}, context_instance=RequestContext(request))
    response.status_code = code
    return response


def handle403(request):
    return pageError(request, 403)


def handler404(request):
    return pageError(request, 404)


def handler500(request):
    return pageError(request, 500)
