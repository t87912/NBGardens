# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Purchase, Employee, Customer
from .forms import YearForm, ContactForm
from django.core.mail import send_mail
from django.db import connection
from collections import namedtuple
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    template = loader.get_template('djangomysqlapp/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
def login(request, username, password):
	username= request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		template = loader.get_template('djangomysqlapp/orders.html')
		context = {
		}
		return HttpResponse(template.render(context, request))
	else:
		# Bad login details were provided. So we can't log the user in.
		print "Invalid login details: {0}, {1}".format(username, password)
		return HttpResponse("Invalid login details supplied.")

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
	order_list = Purchase.objects.order_by('idpurchase')[:10]
	template = loader.get_template('djangomysqlapp/orders.html')
	context = {
	'order_list': order_list,
	}	
	return HttpResponse(template.render(context, request))
	
def order(request, idpurchase):
    return HttpResponse("You're looking at Order %s." % idpurchase)
def results(request, idproduct):
    response = "You're looking at the results of Product %s."
    return HttpResponse(response % idproduct)
def vote(request, idproduct):
    return HttpResponse("You're voting on Product %s." % idproduct)	
def employee(request):
	product_list = Employee.objects.order_by('idemployee')
	template = loader.get_template('djangomysqlapp/employee.html')
	context = {
	'product_list': product_list,
	}
	return HttpResponse(template.render(context, request))
def customer(request):
	product_list = Customer.objects.order_by('idCustomer')
	template = loader.get_template('djangomysqlapp/customer.html')
	context = {
	'product_list': product_list,
	}	
	return HttpResponse(template.render(context, request))
def help(request):
	template = loader.get_template('djangomysqlapp/help.html')
	context = {
	}
	return HttpResponse(template.render(context, request))
def query(request, datestart, dateend):
	cursor = connection.cursor()
	order_list = Employee.objects.raw('''SELECT e.idEmployee, e.firstName, e.lastName, round(SUM(p.salePrice * op.quantity),2) as 'TotalSales' From nbgardensds.Purchase as o Join nbgardensds.PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join nbgardensds.Product as p On op.Pro_idProduct = p.idProduct Join nbgardensds.Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between %(select_cond)s and %(where_cond)s group by e.idEmployee order by 'TotalSales' desc limit 20''', params={'select_cond': datestart, 'where_cond': dateend})
	template = loader.get_template('djangomysqlapp/queryone.html')
	context = {
	'order_list': order_list,
	}
	return HttpResponse(template.render(context, request))
	
def querytwo(request, datestart, dateend):
	cursor = connection.cursor()
	order_list = Customer.objects.raw('''SELECT c.idCustomer, c.firstName, c.lastName, round(SUM(p.salePrice*op.quantity),2) as 'TotalSales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Customer as c On o.cust_idCustomer = c.idCustomer where o.createDate between %(date_start)s and %(date_end)s group by c.idCustomer order by round(SUM(p.salePrice*op.quantity),2) desc limit 20''', params={'date_start': datestart, 'date_end': dateend})
	template = loader.get_template('djangomysqlapp/querytwo.html')
	context = {
	'order_list': order_list,
	}
	return HttpResponse(template.render(context, request))	
def querythree(request, datestart, dateend, amountmin):
	cursor = connection.cursor()
	order_list = Customer.objects.raw('''SELECT c.idCustomer, c.firstName, c.lastName, round(SUM(p.salePrice*op.quantity),2) as 'TotalSales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Customer as c On o.cust_idCustomer = c.idCustomer where o.createDate between %(date_start)s and %(date_end)s group by c.idCustomer having round(SUM(p.salePrice*op.quantity),2) > %(amountmin)s order by round(SUM(p.salePrice*op.quantity),2) desc''', params={'date_start': datestart, 'date_end': dateend, 'amountmin': amountmin})
	template = loader.get_template('djangomysqlapp/querytwo.html')
	context = {
	'order_list': order_list,
	}
	return HttpResponse(template.render(context, request))
def queryfour(request, datestart, dateend):
	cursor = connection.cursor()
	cursor.execute('''SELECT round(sum(p.salePrice*op.quantity),2) as 'TotalSales', round(sum(p.buyPrice*op.quantity),2) as 'TotalCost' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct where o.createDate between %(date_start)s and %(date_end)s''', params={'date_start': datestart, 'date_end': dateend})
	template = loader.get_template('djangomysqlapp/queryfour.html')
	context = {
	'order_list': namedtuplefetchall(cursor),
	}
	return HttpResponse(template.render(context, request))	
def queryfive(request, datestart, dateend, productid):
	cursor = connection.cursor()
	order_list = Customer.objects.raw('''SELECT p.idProduct, round((sum(p.salePrice*op.Quantity) - sum(p.buyPrice*op.Quantity)),2) as 'ReturnonInvestment' From Purchase as o Join PurchaseLines as op On o.idPurchase = op.pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct where o.createDate between %(date_start)s and %(date_end)s and p.idProduct = %(productid)s group by p.idProduct''', params={'date_start': datestart, 'date_end': dateend, 'productid': productid})
	template = loader.get_template('djangomysqlapp/queryfive.html')
	context = {
	'order_list': order_list,
	}
	return HttpResponse(template.render(context, request))
def querysix(request, datestart, dateend):
	cursor = connection.cursor()
	cursor.execute('''SELECT AVG(DATEDIFF(deliveredDate, createDate)) as 'AverageDate' FROM Purchase WHERE createDate BETWEEN %(date_start)s and %(date_end)s''', params={'date_start': datestart, 'date_end': dateend})
	template = loader.get_template('djangomysqlapp/querysix.html')
	context = {
	'order_list': dictfetchall(cursor),
	}
	return HttpResponse(template.render(context, request))
def queryfourteen(request, datestart, dateend, employeeid):
	cursor = connection.cursor()
	order_list = Employee.objects.raw('''SELECT e.idEmployee, o.createDate, round(SUM(p.salePrice*op.quantity),2) as 'Sales' From Purchase as o Join PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join Product as p On op.Pro_idProduct = p.idProduct Join Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between %(date_start)s and %(date_end)s AND e.idEmployee = %(employee_id)s group by e.idEmployee DESC''', params={'date_start': datestart, 'date_end': dateend, 'employee_id': employeeid})
	template = loader.get_template('djangomysqlapp/queryfourteen.html')
	context = {
	'order_list': order_list,
	}
	return HttpResponse(template.render(context, request))
def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
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

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})			
def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]