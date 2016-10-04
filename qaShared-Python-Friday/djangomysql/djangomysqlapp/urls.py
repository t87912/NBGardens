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
    # ex: /polls/5/results/
    url(r'^(?P<idproduct>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<idproduct>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^query/(?P<datestart>[\w\-]+)/(?P<dateend>[\w\-]+)$', views.query, name='query'),
]