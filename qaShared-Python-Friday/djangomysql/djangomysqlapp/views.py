from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Purchase, Employee, Customer
from .forms import YearForm, LoginForm, ContactForm
from django.core.mail import send_mail
from django.db import connection

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
	cursor = connection.cursor()
	#cursor.execute('''SELECT e.idEmployee, e.firstName, e.lastName, round(SUM(p.salePrice * op.quantity),2) as 'Total Sales' From nbgardensds.Purchase as o Join nbgardensds.PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join nbgardensds.Product as p On op.Pro_idProduct = p.idProduct Join nbgardensds.Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between '2015-01-30' and '2016-01-30' group by e.idEmployee order by 'Total Sales' desc limit 20''')
	order_list = Employee.objects.raw('''SELECT e.idEmployee, e.firstName, e.lastName, round(SUM(p.salePrice * op.quantity),2) as 'TotalSales' From nbgardensds.Purchase as o Join nbgardensds.PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join nbgardensds.Product as p On op.Pro_idProduct = p.idProduct Join nbgardensds.Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between '2015-01-30' and '2016-01-30' group by e.idEmployee order by 'Total Sales' desc limit 20''')
	#order_list = cursor.fetchall()
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
	
def query(request, datestart, dateend):
	cursor = connection.cursor()
	order_list = Employee.objects.raw('''SELECT e.idEmployee, e.firstName, e.lastName, round(SUM(p.salePrice * op.quantity),2) as 'TotalSales' From nbgardensds.Purchase as o Join nbgardensds.PurchaseLines as op On o.idPurchase = op. pur_idPurchase Join nbgardensds.Product as p On op.Pro_idProduct = p.idProduct Join nbgardensds.Employee as e On o.emp_idEmployee = e.idEmployee where o.createDate between %(select_cond)s and %(where_cond)s group by e.idEmployee order by 'TotalSales' desc limit 20''', params={'select_cond': datestart, 'where_cond': dateend})
	template = loader.get_template('djangomysqlapp/queryone.html')
	context = {
	'order_list': order_list,
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
def get_year(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = YearForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            year = form.cleaned_data['year']

			
			
			
			
			
			
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = YearForm()
    return render(request, 'product.html', {'form': form})
	

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
	
def jqueryserver(request):
    print "in jqueryserver"
    response_string="hello"
    if request.method == 'GET':
        if request.is_ajax()== True:
            return HttpResponse(response_string,mimetype='text/plain')