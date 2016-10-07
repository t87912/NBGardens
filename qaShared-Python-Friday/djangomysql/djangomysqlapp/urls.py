from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
	url(r'^products/$', views.products, name='products'),
    url(r'^product/(?P<idproduct>[0-9]+)/$', views.product, name='product'),
	url(r'^help/$', views.help, name='help'),
	url(r'^orders/$', views.orders, name='orders'),
	url(r'^orders_paginate/(?P<limitstart>[0-9]+)/$', views.orders_paginate, name='orders_paginate'),
	url(r'^login/(?P<uname>[\w\-]+)/(?P<pword>[\w\-]+)$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
    url(r'^order/(?P<idpurchase>[0-9]+)/$', views.order, name='order'),	
	url(r'^employee/$', views.employee, name='employee'),
	url(r'^customer/$', views.customer, name='customer'),
    url(r'^(?P<idproduct>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<idproduct>[0-9]+)/vote/$', views.vote, name='vote'),
	
	url(r'^create_product/(?P<productnamenew>[\w\-]+)/(?P<descriptionnew>[\w\-]+)/(?P<buypricenew>[\w\-]+)/(?P<salepricenew>[\w\-]+)/(?P<quantitynew>[\w\-]+)$', views.create_product, name='create_product'),
	
	url(r'^query/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.query, name='query'),
	url(r'^querytwo/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.querytwo, name='querytwo'),
	url(r'^querythree/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<amountmin>[\w\-]+)$', views.querythree, name='querythree'),
	url(r'^queryfour/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.queryfour, name='queryfour'),
	url(r'^queryfive/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<productid>[\w\-]+)$', views.queryfive, name='queryfive'),
	url(r'^querysix/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.querysix, name='querysix'),

	
	
	
	
	
	url(r'^querythirteen/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<productid>[\w\-]+)$', views.querythirteen, name='querythirteen'),
	url(r'^queryfourteen/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)/(?P<employeeid>[\w\-]+)$', views.queryfourteen, name='queryfourteen'),
	
	url(r'^dashboard_total_orders/$', views.dashboard_total_orders, name='dashboard_total_orders'),
	url(r'^dashboard_total_customers/$', views.dashboard_total_customers, name='dashboard_total_customers'),
	url(r'^dashboard_most_popular_product/$', views.dashboard_most_popular_product, name='dashboard_most_popular_product'),
]