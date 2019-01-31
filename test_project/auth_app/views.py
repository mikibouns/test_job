from django.shortcuts import render, HttpResponseRedirect
from . forms import UserLoginForm
from django.contrib import auth


def login(request):
    current_path = request.META.get('HTTP_REFERER')
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(current_path)

    return HttpResponseRedirect(current_path)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

