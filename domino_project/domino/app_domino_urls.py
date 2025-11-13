from django.urls import path
from . import views, app_views
from .app_views import auth_views, product_views, admin_views, category_views, user_views, menu_views, cart_views


urlpatterns = [
    path("", menu_views.home, name="/"),
    path("contacts/", menu_views.contact_menu, name="contacts"),
    path("menu/", menu_views.menu_menu, name="menu"),
    path("carts/", menu_views.cart_menu, name="carts"),

    path('manager/dashboard/', admin_views.dashboard, name='admin_dashboard'),
    path('login/', auth_views.user_login, name='login'),
    path('logout/', auth_views.user_logout, name='logout'),
    path('register/', auth_views.register, name='register'),
    path('settings/', menu_views.profile_settings, name='profile_settings'),
    path('change-password/', menu_views.change_password, name='change_password'),
    path('profile/', user_views.profile_settings, name='profile_settings'),

    # User Management
    path('manager/users/', user_views.index, name='user_index'),
    path('manager/users/show/', user_views.show, name='user_show'),
    path('manager/users/create/', user_views.create, name='user_create'),
    path('manager/users/delete/<int:id>/', user_views.delete, name='user_delete'),
    path('manager/users/edit/<int:id>/', user_views.edit, name='user_edit'),
    path('manager/users/update/<int:id>/', user_views.update, name='user_update'),

    # Product Management
    path('manager/products/', product_views.index, name='product_index'),
    path('manager/products/show/', product_views.show, name='product_show'),
    path('manager/products/create/', product_views.create, name='product_create'),
    path('manager/products/delete/<int:id>/', product_views.delete, name='product_delete'),
    path('manager/products/edit/<int:id>/', product_views.edit, name='product_edit'),
    path('manager/products/update/<int:id>/', product_views.update, name='product_update'),

    # Category Management
    path('manager/categories/', category_views.index, name='category_index'),
    path('manager/categories/show/', category_views.show, name='category_show'),
    path('manager/categories/create/', category_views.create, name='category_create'),
    path('manager/categories/delete/<int:id>/', category_views.delete, name='category_delete'),
    path('manager/categories/edit/<int:id>/', category_views.edit, name='category_edit'),
    path('manager/categories/update/<int:id>/', category_views.update, name='category_update'),

    # Invoice
    path('invoice/', cart_views.process_checkout, name='process_checkout'),
    path('create-invoice/', cart_views.create_invoice, name='create_invoice'),

]


