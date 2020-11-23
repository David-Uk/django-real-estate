from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Passwords do not match')
            messages.error(request, 'Passwords do not match')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
