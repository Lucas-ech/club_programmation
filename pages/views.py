from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from pages.models import Page
from pages.forms import PageForm


def homepage(request):
    return render(request, 'pages/pages.html', {'page': Page.objects.filter(name='accueil')[0]})


def presentation(request):
    return render(request, 'pages/pages.html', {'page': Page.objects.filter(name='presentation')[0]})


@login_required
@permission_required('pages.change_page')
def edit(request, name):
    page = get_object_or_404(Page, name=name)

    if request.method == 'POST':
        form = PageForm(request.POST or None, instance=page)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/edit.html', locals())
