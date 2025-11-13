# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from . models import Product, Category
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from .. app_views import login_register
# from .forms import UserForm, ProfileForm
#
#
# def home(request):
#     return render(request, "pages/index.html")
#
#
# # load all the product from database using category as separation
# # when clicked on menu
# def menu_menu(request):
#     categories = Category.objects.prefetch_related('products').all()
#     return render(request, 'pages/menu.html', {'categories': categories})
#
#
# def cart_menu(request):
#     return render(request, "pages/cart.html")
#
#
# def contact_menu(request):
#     return render(request, "pages/contact.html")
#
#
# def register_view(request):
#     return render(request, "pages/register.html")
#
#
# def login_view(request):
#     requests = check_login
#     return render(request, 'pages/login.html')
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')
#
#
# # @login_required
# def profile_settings(request):
#     # user = request.user
#     # profile = user.profile
#     #
#     # if request.method == 'POST':
#     #     user_form = UserForm(request.POST, instance=user)
#     #     profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
#     #
#     #     if user_form.is_valid() and profile_form.is_valid():
#     #         user_form.save()
#     #         profile_form.save()
#     #         messages.success(request, 'Your profile was updated successfully.')
#     #         return redirect('accounts:profile_settings')
#     #     else:
#     #         messages.error(request, 'Please correct the error(s) below.')
#     # else:
#     #     user_form = UserForm(instance=user)
#     #     profile_form = ProfileForm(instance=profile)
#     #
#     # password_form = PasswordChangeForm(user)
#     #
#     # return render(request, 'accounts/profile_settings.html', {
#     #     'user_form': user_form,
#     #     'profile_form': profile_form,
#     #     'password_form': password_form,
#     # })
#     return render(request, 'accounts//profile_settings.html')
#
#
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important to keep user logged in
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('accounts:profile_settings')
#         else:
#             messages.error(request, 'Please correct the error below.')
#             return redirect('accounts:profile_settings')
#     else:
#         return redirect('accounts:profile_settings')
#
