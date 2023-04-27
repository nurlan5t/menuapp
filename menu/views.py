from django.shortcuts import render
from menu.models import Menu, Category, Product


def menus_list(request):
    menus = Menu.objects.all()
    context = {'menus_list': menus}
    return render(request, 'menu/menus_list.html', context)


def menu_detail(request, pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu_detail': menu}
    return render(request, 'menu/menu_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories_list': categories}
    return render(request, 'menu/categories_list.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {'products_list': products}
    return render(request, 'menu/products_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product_detail': product}
    return render(request, 'menu/product_detail.html', context)
