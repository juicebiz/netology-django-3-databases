from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'id')
    match sort:
        case "min_price":
            order = "price"
        case "max_price":
            order = "-price"
        case _:
            order = sort

    phones = Phone.objects.order_by(order).all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
