from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .. models import User


def user_login(request):
    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'pages/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # better than '/'


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')  # prevent logged-in users from registering again

    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # === Validation ===
        if not all([email, first_name, phone, password, password2]):
            messages.error(request, "All fields are required.")
            return render(request, 'account/register.html')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'account/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, 'account/register.html')

        try:
            user = User.objects.create_user(
                username=email,      # using email as username
                email=email,
                password=password,
                first_name=first_name,
                phone=phone,
                gender=gender
            )
            user.save()

            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, 'account/register.html')

    return render(request, 'account/register.html')


def redirect_based_on_role(user):
    """Redirect users based on their role"""
    if hasattr(user, 'role'):
        if user:
            return redirect('/profile/')
        else:
            return redirect('/login/')
    else:
        return redirect('loging/')
