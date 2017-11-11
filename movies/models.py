from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Productor(models.Model):
	name= models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	duration = models.DurationField(blank=True, null=True)
	summary = models.TextField()
	director = models.CharField(max_length=200)
	image = models.ImageField(upload_to='pelis')
	productor = models.ForeignKey(Productor, related_name='movies', blank=True, null=True)

	def __str__(self):
		return self.title

class Actor(models.Model):
	name = models.CharField(max_length=100)
	movie = models.ManyToManyField(Movie, related_name='actors')

	def __str__(self):
		return self.name

class Comment(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	movie = models.ForeignKey(Movie, related_name='comments')
	user = models.ForeignKey(User,related_name='comments')

	def __str__(self):
		return self.title






