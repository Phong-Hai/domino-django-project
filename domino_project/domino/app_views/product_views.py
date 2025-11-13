from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from domino.models import Product, Category


@login_required(login_url='/login/')
def index(request):
    if request.method == "POST":
        search_item = request.POST['search_item']
        products = Product.objects.filter(name__contains=search_item)  # Changed
        count_item = products.count()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {"products": page_obj, "count_item": count_item, "title": "Product List"}  # Changed
    else:
        products = Product.objects.all().order_by('id')
        count_item = products.count()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {"products": page_obj, "count_item": count_item, "title": "Product List"}

    return render(request, "admin/product/index.html", context=data)


@login_required(login_url='/login/')
def show(request):
    categories = Category.objects.all()  # Get all categories from database
    data = {"title": "Add Product", "categories": categories}
    return render(request, "admin/product/create.html", context=data)


@login_required(login_url='/login/')
def edit(request, id):
    product = Product.objects.get(pk=id)
    categories = Category.objects.all()
    data = {"product": product, "title": "Update Product", "categories": categories}
    return render(request, "admin/product/update.html", context=data)


@login_required(login_url='/login/')
def create(request):
    try:
        if request.method == 'POST':
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)

            Product.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                price=request.POST.get('price'),
                category=category,
                stock_qty=request.POST.get('stock_qty'),
                image=request.FILES.get('image')
            )
            messages.success(request, 'Product added successfully!')
            return redirect('/manager/products/')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    categories = Category.objects.all()
    return render(request, "admin/product/create.html", {"categories": categories})


@login_required(login_url='/login/')
def update(request, id):
    if request.method == 'POST':
        try:
            product_exist = Product.objects.get(pk=id)
            category_id = request.POST['category']
            category = Category.objects.get(id=category_id)

            product_exist.name = request.POST['name']
            product_exist.description = request.POST['description']
            product_exist.price = request.POST['price']
            product_exist.category = category
            product_exist.stock_qty = request.POST['stock_qty']
            if request.FILES.get('image'):
                product_exist.image = request.FILES['image']
            product_exist.full_clean()
            product_exist.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('/manager/products/')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect(f'/manager/products/edit/{id}/')
    else:
        return redirect(f'/manager/products/edit/{id}/')

@login_required(login_url='/login/')
def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('/manager/products/')