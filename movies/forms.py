from django import forms
from .models import Movie, Productor, Actor, Comment

#class MovieForm(forms.Form):
#	title = forms.CharField()
	#duration = forms.DurationField(required=False)
#	summary = forms.CharField(required=False)
#	director = forms.CharField(required=False)
#	image = forms.ImageField(required=False)

class MovieFormChido(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Titulo de la pelicula','class':'requerido'}))
	class Meta: #esta si es de awebo chavos
		model = Movie
		fields = ['title','duration','summary','director','image','productor']


class ProductorForm(forms.ModelForm):
	class Meta:
		model = Productor
		fields = '__all__'

class ActorForm(forms.ModelForm):
	class Meta:
		model = Actor
		fields = '__all__'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['title','text']
