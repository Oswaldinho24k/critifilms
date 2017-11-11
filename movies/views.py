from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Movie, Comment
from .forms import MovieFormChido, ProductorForm, ActorForm, CommentForm
from django.http import HttpResponse

# Create your views here.

class MovieListView(View):
	def get(self, request):
		template_name="movies/list.html"
		movies = Movie.objects.all()
		context={
			'movies':movies
		}
		return render(request, template_name, context)


class MovieDetailView(View):
	def get(self, request, id):
		template_name = "movies/detail.html"
		form = CommentForm()
		
		movie = get_object_or_404(Movie, id=id) #Movie.objects.get(id=id)
		comentarios = Comment.objects.all().filter(movie=movie)
		context = {
			'movie':movie,
			'form':form,
			'comentarios':comentarios
		}
		return render(request, template_name, context)

	def post(self, request, id):
		form = CommentForm(request.POST)

		if form.is_valid():
			form_save = form.save(commit=False)
			form_save.user = request.user
			form_save.movie = Movie.objects.get(id=id)
			form_save.save()
			return redirect('/movies/',id)


class AddMovie(View):
	def get(self, request):
		template_name="movies/addMovieChido.html"
		form = MovieFormChido()
		context = {'form':form}
		return render(request, template_name, context)

	def post(self, request):

		form = MovieFormChido(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			return HttpResponse("Llenaste mal los datos")

		return redirect('/movies/')

class AddProductor(View):
	def get(self,request):
		template_name="movies/addProductor.html"
		form = ProductorForm()
		context = {'form':form}
		return render(request, template_name, context)

	def post(self,request):
		form = ProductorForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			pass

		return redirect('/movies/')

class AddActor(View):
	def get(self,request):
		template_name="movies/addActor.html"
		form = ActorForm()
		context = {'form':form}
		return render(request, template_name, context)

	def post(self,request):
		form = ActorForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			pass

		return redirect('/movies/')

