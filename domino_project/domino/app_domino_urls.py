from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="/"),
    path("contacts/", views.contact_menu, name="contacts"),
    path("menu/", views.menu_menu, name="menu"),
    path("carts/", views.cart_menu, name="carts"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('settings/', views.profile_settings, name='profile_settings'),
    path('change-password/', views.change_password, name='change_password'),
    path('profile/', views.profile_settings, name='profile_settings'),
]


