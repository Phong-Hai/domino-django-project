from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

@login_required(login_url='/login/')
def dashboard(request):
    user_role = getattr(request.user, 'role', 'customer')

    # Check if user has permission to access admin dashboard
    if user_role not in ['admin', 'user']:
        messages.error(request, 'You do not have permission to access this page')
        return redirect('/')

    context = {
        'user_role': user_role,
        'can_edit': user_role == 'admin',
        'can_add_user': user_role in ['admin', 'user'],
    }

    return render(request, 'admin/dashboard.html', context)