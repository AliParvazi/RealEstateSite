from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'user you enterd is invalid.')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        # Set incoming Data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validations
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or password != password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is taken.')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is taken.')
            if password != password2:
              messages.error(request, 'You ass hole! fill password fields correctly.')
            
            return redirect('register')    
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, 'You registered successflluy.')
            return redirect('dashboard')
    return render(request, 'accounts/register.html')


def dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not Logged in.\n You Should Login first!')
        return redirect('login')
    return render(request, 'accounts/dashboard.html')
