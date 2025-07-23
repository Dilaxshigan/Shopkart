from django.shortcuts import render, redirect
from shop.form import CustomUserForm
from .models import *
from django.contrib import messages

def home(request):
    products = Product.objects.filter(trending=1)
    return render(request,"shop/index.html ", {"products": products})

def login_page(request):
    return render(request, "shop/login.html ")

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success! You can Login Now.")
            return redirect('/login')  # Only redirect if valid
    return render(request, "shop/register.html", {'form': form})

def category(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/category.html ", {"category":category})

def categoryView(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/products.html", {"products":products, "category_name":name})
    else:
        messages.warning(request, 'No such category exists')
        return redirect('category')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request, "shop/product_details.html", {"products": products})
        else:
            messages.error(request, 'No such product exists')
            return redirect('category')
    else:
        messages.error(request, 'No such category exists')
        return redirect('category')
