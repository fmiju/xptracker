from tracker.models import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response

def index(request):
	
	if 'dname' in request.GET:
		n = request.GET['dname']
	dev = Developer.objects.get(name=n)
	tasks = Task.objects.filter(developer=dev)
	stories = Story.objects.all()
	devsWork = []
	actualTaskTime()
	for s in stories:
		devTasks = tasks.filter(story=s)
		if devTasks:
			devsWork.append({'story':s, 'time':storyTime(devTasks), 'tasks':devTasks})
	context = {
		'devName': n,
		'devsWork': devsWork
	}
	return render(request, 'index.html', context)

def pickDeveloper(request):
	context = {
		'names': Developer.objects.all()
	}
	return render(request, 'pick_dev.html', context)


def storyTime(devTasks):
	time = 0
	for t in devTasks:
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
			
