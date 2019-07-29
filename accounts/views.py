from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(id=request.POST['id'])
                return render(request, 'accounts/signup.html', {'error': '우짜노 이거 있는데'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['id'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('blogapp')
        else:
            return(request, 'accounts/signup.html', {'error': '마 단디 입력해봐라'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, id=id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'accounts/login.html', {'error': '아닌데'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blogapp')
    return render(request, 'accounts/signup.html')
