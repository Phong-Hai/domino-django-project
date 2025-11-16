from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from domino.models import Category

@login_required(login_url='/login/')
def index(request):
    if request.method == "POST":
        search_item = request.POST['search_item']
        categories = Category.objects.filter(name__contains=search_item)
        count_item = categories.count()
        paginator = Paginator(categories, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {"categories": page_obj, "count_item": count_item, "title": "Category List"}
    else:
        categories = Category.objects.all().order_by('id')
        count_item = categories.count()
        paginator = Paginator(categories, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {"categories": page_obj, "count_item": count_item, "title": "Category List"}

    return render(request, "admin/category/index.html", context=data)

@login_required(login_url='/login/')
def show(request):
    data = {"title": "Add Category"}
    return render(request, "admin/category/create.html", context=data)

@login_required(login_url='/login/')
def create(request):
    try:
        if request.method == 'POST':
            Category.objects.create(
                category_name=request.POST.get('category_name')
            )
            messages.success(request, 'Category added successfully!')
            return redirect('/manager/categories/')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return render(request, "admin/category/create.html")

@login_required(login_url='/login/')
def delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('/manager/categories/')

@login_required(login_url='/login/')
def edit(request, id):
    category = Category.objects.get(pk=id)
    data = {"category": category, "title": "Update Category"}
    return render(request, "admin/category/update.html", context=data)

@login_required(login_url='/login/')
def update(request, id):
    if request.method == 'POST':
        category_exist = Category.objects.get(pk=id)
        category_exist.category_name = request.POST['category_name']
        category_exist.full_clean()
        category_exist.save()
        messages.success(request, 'Category updated successfully!')
        return redirect('/manager/categories/')
    else:
        return redirect(f'/manager/categories/edit/{id}/')