from django.contrib.auth.models import User
from django.shortcuts import render


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username, '', password)
        return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})