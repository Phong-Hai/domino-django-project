from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="/"),
    path("contacts/", views.contact_menu, name="contacts"),
    path("menu/", views.menu_menu, name="menu"),
    path("carts/", views.cart_menu, name="carts"),
    path('invoice/', views.process_checkout, name='process_checkout'),


]


