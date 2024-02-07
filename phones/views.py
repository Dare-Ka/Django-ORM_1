from django.shortcuts import render, redirect
from phones.models import Phone
from django.db.models.functions import Lower


def index(request):
    return redirect('catalog')


def show_catalog(request):
    order = {
        'min_price': 'price',
        'max_price': '-price',
        'name': 'name',
        None: 'pk'
    }
    phones = Phone.objects.all().order_by(order[request.GET.get('sort')])
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug__contains=slug).first()
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)