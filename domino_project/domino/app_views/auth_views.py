from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

def user_login(request):
    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect_based_on_role(user)
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'auth/login.html')

def redirect_based_on_role(user):
    """Redirect users based on their role"""
    if hasattr(user, 'role'):
        if user.role in ['admin', 'staff']:
            return redirect('/manager/dashboard/')
        else:
            return redirect('/')
    else:
        return redirect('/')

def user_logout(request):
    """Handle user logout"""
    logout(request)
    return redirect('/')
