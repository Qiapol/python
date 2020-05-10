from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic import CreateView

from .models import BoardModel


# 以下のsignupfuncのtry, exceptは直感に反する。try内の処理が異常時の処理分になっている。これはテストを先に書いた上でリファクタリングを行う。


def signupfunc(request):
    """
    create user function
    :param request:
    :return:
    """
    if request.method == 'POST':
        signup_username = request.POST['username']
        signup_password = request.POST['password']
        try:
            User.objects.get(username=signup_username)
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})
        except:
            user = User.objects.create_user(signup_username, '', signup_password)
            return render(request, 'signup.html', {})
    return render(request, 'signup.html')


def loginfunc(request):
    """
    Login function
    :param request:
    :return:
    """
    if request.method == 'POST':
        login_username = request.POST['username']
        login_password = request.POST['password']
        user = authenticate(request, username=login_username, password=login_password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('signup')
    return render(request, 'login.html')


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


@login_required
def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def logoutfunc(request):
    logout(request)
    return redirect('login')


@login_required()
def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')


@login_required
def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    login_user = request.user.get_username()
    if login_user in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + login_user
        post.save()
    return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
