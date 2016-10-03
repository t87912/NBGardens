from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Purchase
from .forms import YearForm, LoginForm

# Create your views here.
def index(request):
    latest_question_list = Product.objects.order_by('idproduct')[:5]
    template = loader.get_template('djangomysqlapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def products(request):
	product_list = Product.objects.order_by('idproduct')
	template = loader.get_template('djangomysqlapp/products.html')
	context = {
	'product_list': product_list,
	}
	return HttpResponse(template.render(context, request))
def product(request, idproduct):
    return HttpResponse("You're looking at Product %s." % idproduct)
def orders(request):
	order_list = Purchase.objects.order_by('idpurchase')
	template = loader.get_template('djangomysqlapp/orders.html')
	context = {
	'order_list': order_list[:10],
	}
	return HttpResponse(template.render(context, request))
	
def order(request, idpurchase):
    return HttpResponse("You're looking at Order %s." % idpurchase)
def results(request, idproduct):
    response = "You're looking at the results of Product %s."
    return HttpResponse(response % idproduct)
def vote(request, idproduct):
    return HttpResponse("You're voting on Product %s." % idproduct)	