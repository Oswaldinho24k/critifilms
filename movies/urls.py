from django.conf.urls import url
from .views import MovieListView, MovieDetailView, AddMovie, AddProductor, AddActor

urlpatterns = [
	url(r'^$', MovieListView.as_view()),
	url(r'^(?P<id>[0-9]+)/$', MovieDetailView.as_view()),
	url(r'^new/$', AddMovie.as_view()),
	url(r'^productor/new/$', AddProductor.as_view()),
	url(r'actores/new/$', AddActor.as_view())
]