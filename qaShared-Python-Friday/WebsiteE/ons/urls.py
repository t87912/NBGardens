from django.conf.urls import url
from . import views

app_name = 'ons'
urlpatterns= [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='request'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
