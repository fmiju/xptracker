from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
)
