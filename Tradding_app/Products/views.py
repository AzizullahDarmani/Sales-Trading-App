from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required 


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_list')
    else:
        product_form = ProductForm() 
    
    return render(request, 'add_product.html', {'product_form':product_form})



def product_list(request):
    category_id = request.GET.get('category')  # Get selected category from query parameters
    products = Product.objects.all()
    categories = Category.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)  # Filter products by category

    return render(request, 'product_list.html', {'products': products, 'categories': categories})




def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save() 
            return redirect('add_product')
    else:
        category_form = CategoryForm()

    return render(request, 'add_category.html', {'category_form':category_form})



def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method== 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_confirm.html', {'product': product})