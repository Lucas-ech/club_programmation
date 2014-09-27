from django.contrib import admin
from projects.models import Project, Comment, Language


admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Language)
