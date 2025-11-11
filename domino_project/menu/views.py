from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem

def menu_view(request):
    products = Product.objects.all()
    return render(request, 'menu/menu.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')

def cart_view(request):
    items = CartItem.objects.all()
    total = sum(item.total_price for item in items)
    return render(request, 'menu/cart.html', {'items': items, 'total': total})
