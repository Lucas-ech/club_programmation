from django import forms
from projects.models import Project, Comment


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('author', 'slug')
        labels = {
            'title': 'Titre',
            'content': '',
            'source': 'Adresse de téléchargement',
            'language': 'Langage',
            'online': 'Mettre en ligne'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'project')
        labels = {
            'content': '',
        }
