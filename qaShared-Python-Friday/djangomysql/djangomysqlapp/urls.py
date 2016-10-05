from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
	url(r'^products/$', views.products, name='products'),
    url(r'^product/(?P<idproduct>[0-9]+)/$', views.product, name='product'),
	url(r'^orders/$', views.orders, name='orders'),
    url(r'^order/(?P<idpurchase>[0-9]+)/$', views.order, name='order'),	
	url(r'^employee/$', views.employee, name='employee'),
	url(r'^customer/$', views.customer, name='customer'),
    url(r'^(?P<idproduct>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<idproduct>[0-9]+)/vote/$', views.vote, name='vote'),
	
	url(r'^query/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.query, name='query'),
	url(r'^querytwo/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.querytwo, name='querytwo'),
	url(r'^querythree/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<amountmin>[\w\-]+)$', views.querythree, name='querythree'),
	url(r'^queryfour/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.queryfour, name='queryfour'),
	url(r'^queryfive/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<productid>[\w\-]+)$', views.queryfive, name='queryfive'),
	url(r'^querysix/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.querysix, name='querysix'),

	
	
	
	
	
	
	url(r'^queryfourteen/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<employeeid>[\w\-]+)$', views.queryfourteen, name='queryfourteen'),
]