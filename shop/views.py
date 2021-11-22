from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from .models import Product, User
from .forms import RequestListForm


def index_test(request):
    s = "Список объявлений\n\n"
    for prod in Product.objects.order_by('available'):
        s += prod.title + '\r\n' + prod.description + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')


def index(request):
    template = loader.get_template('index.html')
    products = Product.objects.order_by('available')
    context = {'products': products}
    return HttpResponse(template.render(context, request))


def shop_page(request):
    return redirect('shop/')


def product_page(request, prod_id):
    template = loader.get_template('product.html')
    if Product.objects.filter(pk=prod_id).exists():
        prod = Product.objects.get(pk=prod_id)
        context = {'prod': prod}
        return HttpResponse(template.render(context, request))
    else:
        s = "Нет такого товара"
        context = {'prod': s}
        return HttpResponse(template.render(context, request))


def request_page(request):
    error = ""
    if request.method == "POST":
        form = RequestListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Ошибка в полях ввода"

    form = RequestListForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'request.html', data)
