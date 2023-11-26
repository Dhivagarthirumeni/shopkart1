from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"shop/templates/shop/index.html")
def register(request):
    return render(request,"shop/templates/shop/register.html")
def collections(request):
    catagory = Category.objects.filter(status=0)
    return render(request,"shop/templates/shop/collections.html",{"catagory":catagory})
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/templates/shop/products/product.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"no such catagory found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/templates/shop/products/product_view.html",{"products":products})
        else:
            messages.error(request,"no such catagory found")
            return redirect("collections")
    else:
        messages.error(request,"no such catagory found")
        return redirect("collections")
