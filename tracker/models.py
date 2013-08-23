from django.db import models

STR_LENGTH = 50

class Developer(models.Model):
	name = models.CharField(max_length=STR_LENGTH)
	def __unicode__(self):
		return self.name

class Story(models.Model):
	value = models.CharField(max_length=255)
	estTime = models.IntegerField(default=0)
	def __unicode__(self):
		return self.value

class Task(models.Model):
	value = models.CharField(max_length=255)
	estTime = models.IntegerField(default=0)
	realTime = models.IntegerField(default=0)
	developer = models.ForeignKey(Developer)
	iteration = models.CharField(max_length=STR_LENGTH)
	story = models.ForeignKey(Story)
	def __unicode__(self):
		return self.value

class RealTime(models.Model):
	value = models.IntegerField(default=0)
	task = models.ForeignKey(Task)
	def __unicode__(self):
		return str(self.value)
