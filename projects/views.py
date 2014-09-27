from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.template.defaultfilters import slugify
from projects.models import Project, Comment
from projects.forms import ProjectForm, CommentForm


# Retourne la différence entre deux listes
def listDiff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]


def list(request):
    if request.user.is_authenticated():
        projects = Project.objects.order_by('created')[:10:-1]
    else:
        projects = Project.objects.filter(online=True).order_by('created')[:10:-1]
    return render(request, 'projects/list.html', {'projects': projects})


def view(request, slug):
    if request.user.is_authenticated():
        project = get_object_or_404(Project, slug__iexact=slug)
    else:
        project = get_object_or_404(Project, slug__iexact=slug, online=True)
    comments = Comment.objects.filter(project=project)
    if request.user.has_perm('projects.add_comment'):
        form = CommentForm()
    return render(request, 'projects/view.html', locals())


@require_http_methods(["POST"])
@permission_required('projects.add_comment')
def save_comment(request, slug):
    project = get_object_or_404(Project, slug__iexact=slug)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.project = project
        comment.author_id = request.user.id
        comment.save()
    return redirect('projects_view', slug=slug)


@permission_required('projects.add_project')
@requires_csrf_token
def edit(request, slug):
    if not request.user.is_superuser:
        project = get_object_or_404(Project, slug__iexact=slug, author=request.user)
    else:
        project = get_object_or_404(Project, slug__iexact=slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=project)

        if form.is_valid():
            form.save()

            # Si il n'y a plus d'auteurs dans le formulaire on ne met pas à jour
            authors_form = request.POST.getlist('authors')
            if len(authors_form) > 0:
                authors_project = []
                for author in project.author.all():
                    authors_project.append(author.username)

                toAdd = listDiff(authors_form, authors_project)
                toRemove = listDiff(authors_project, authors_form)

                # On ajoute les auteurs manquants
                for item in toAdd:
                    user = User.objects.filter(username=item)[0]
                    if user:
                        project.author.add(user.id)

                # On supprime les autres auteurs
                for item in toRemove:
                    user = User.objects.filter(username=item)[0]
                    if user:
                        project.author.remove(user.id)

            return redirect('projects_view', slug=slug)
    else:
            form = ProjectForm(instance=project)

    return render(request, 'projects/edit.html', {'form': form, 'project': project})


@permission_required('projects.add_project')
@requires_csrf_token
def create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)

            # On vérifie que le slug n'existe pas en bdd
            i = 0
            found = False
            while not found:
                if i > 0:
                    slug = slugify(form.cleaned_data['title']) + '-' + str(i)
                else:
                    slug = slugify(form.cleaned_data['title'])
                if Project.objects.filter(slug__iexact=slug).count() == 0:
                    project.slug = slug
                    found = True
                i += 1

            project.save()
            project.author.add(request.user.id)
            return redirect('projects_view', slug=slug)
    else:
            form = ProjectForm()

    return render(request, 'projects/edit.html', {'form': form})
