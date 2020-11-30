from django.shortcuts import render
from .models import Product


def home(request):
    if request.user.is_authenticated:
        username_is = "Delroy Brown"
        context = {"username_is": username_is}
    else:
        context = {"username_is": "Stranger Danger!"}
    template = 'products/home.html'
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)
