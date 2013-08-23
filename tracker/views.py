from tracker.models import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
	#devs = Developer.objects.get(name='Anna Squid')	
	n = 'Britta Helgesson'
	dev = Developer.objects.get(name=n)
	tasks = Task.objects.filter(developer=dev)
	stories = Story.objects.all()
	devsWork = []
	actualTaskTime()
	for s in stories:
		devTasks = tasks.filter(story=s)
		if devTasks:
			devsWork.append({'story':s, 'time':storyTime(s), 'tasks':devTasks})
	context = {
		'devName': n,
		'devsWork': devsWork
	}
	return render(request, 'index.html', context)

def storyTime(s):
	storiesTasks = Task.objects.filter(story=s)
	time = 0
	for t in storiesTasks:
		time += t.realTime
	return time

def actualTaskTime():
	tasks = Task.objects.all()
	for t in tasks:
		rTime = RealTime.objects.filter(task=t)
		timeForTask = 0
		for r in rTime:
			timeForTask += r.value
		t.realTime = timeForTask
		t.save()
			
