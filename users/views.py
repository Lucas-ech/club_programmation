import json
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from users.forms import LoginForm


def login(request):
    error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"].lower()
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect(request.GET.get('next', '/'))
            else:
                error = True
    else:
        form = LoginForm()
    return render(request, 'users/login.html', locals())


def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
    return redirect('homepage')


def myaccount(request):
    return render(request, 'users/myaccount.html', {'user': request.user})


def configuration(request):
    return render(request, 'users/configuration.html')


@require_http_methods(["GET"])
def getUsersByUsername(request):
    if not HttpRequest.is_ajax(request):
        return HttpResponse(status=404)
    term = request.GET.get('term', '')
    users = User.objects.filter(username__startswith=term)

    usernames = []
    for user in users:
        usernames.append(user.username)

    return HttpResponse(json.dumps(usernames), content_type="application/json")
