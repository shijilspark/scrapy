from django.conf.urls import patterns, url

from scrapdeals import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^subscribe/$',views.subscribe, name='subscribe'),
)