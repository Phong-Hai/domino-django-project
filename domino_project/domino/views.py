from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from . models import Product, Category


def home(request):
    return render(request, "pages/index.html")


# load all the product from database using category as separation
# when clicked on menu
def menu_menu(request):
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'pages/menu.html', {'categories': categories})


def cart_menu(request):
    return render(request, "pages/cart.html")


def contact_menu(request):
    return render(request, "pages/contact.html")



