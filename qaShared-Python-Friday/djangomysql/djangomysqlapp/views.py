from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Purchase
from .forms import YearForm, LoginForm, ContactForm
from django.core.mail import send_mail

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
	
def get_year(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = YearForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = YearForm()

    return render(request, 'product.html', {'form': form})

def get_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'home.html', {'form': form})
	
if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')