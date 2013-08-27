from django.conf.urls import patterns, include, url

from tracker import views

urlpatterns = patterns('', 
	url(r'^select/$', views.pickDeveloper),
	url(r'^view/$', views.index),
)
