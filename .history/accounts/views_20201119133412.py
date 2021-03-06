from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

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
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)         
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('/')
                    user.save()
                    messages.success(request, 'You are can now log in')
                    return redirect('login')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
