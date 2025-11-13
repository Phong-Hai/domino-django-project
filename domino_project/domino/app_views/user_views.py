from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from domino.models import User

@login_required(login_url='/login/')
def index(request):
    if request.method == "POST":
        search_item = request.POST['search_item']
        users = User.objects.filter(first_name__contains=search_item)
        count_item = users.count()
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            "users": page_obj,
            "count_item": count_item,
            "title": "User List",  # Changed
            "search_action": "/manager/users/",
            "current_model": "user"
        }
    else:
        users = User.objects.all().order_by('id')
        count_item = users.count()
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            "users": page_obj,
            "count_item": count_item,
            "title": "User List",
            "search_action": "/manager/users/",
            "current_model": "user"
        }

    return render(request, "admin/user/index.html", context=data)

@login_required(login_url='/login/')
def show(request):
    data = {"title": "Add User"}  # Changed
    return render(request, "admin/user/create.html", context=data)

@login_required(login_url='/login/')
def create(request):
    try:
        if request.method == 'POST':
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
            )

            # Add optional fields only if provided
            if request.POST.get('first_name'):
                user.first_name = request.POST.get('first_name')
            if request.POST.get('last_name'):
                user.last_name = request.POST.get('last_name')
            if request.POST.get('email'):
                user.email = request.POST.get('email')
            if request.POST.get('gender'):
                user.gender = request.POST.get('gender')
            if request.POST.get('phone'):
                user.phone = request.POST.get('phone')
            if request.POST.get('address'):
                user.address = request.POST.get('address')
            if request.POST.get('role'):
                user.role = request.POST.get('role')

            user.save()

            messages.success(request, 'User added successfully!')
            return redirect('/manager/users/')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return render(request, "admin/user/create.html")

@login_required(login_url='/login/')
def edit(request, id):
    user = User.objects.get(pk=id)
    data = {"user": user, "title": "Update User"}
    return render(request, "admin/user/update.html", context=data)  # Updated path


@login_required(login_url='/login/')
def update(request, id):
    if request.method == 'POST':
        user_exist = User.objects.get(pk=id)
        user_exist.username = request.POST['username']
        user_exist.first_name = request.POST['first_name']
        user_exist.last_name = request.POST['last_name']
        user_exist.email = request.POST['email']
        user_exist.gender = request.POST['gender']
        user_exist.phone = request.POST['phone']
        user_exist.address = request.POST['address']
        user_exist.role = request.POST['role']

        if request.POST['password']:
            user_exist.set_password(request.POST['password'])

        user_exist.save()
        messages.success(request, 'User updated successfully!')
        return redirect('/manager/users/')
    else:
        return redirect(f'/manager/users/edit/{id}/')

@login_required(login_url='/login/')
def delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    messages.success(request, 'User deleted successfully!')
    return redirect('/manager/users/')