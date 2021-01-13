from django.urls import path
from . import views

urlpatterns = [

	path("joseph", views.joseph, name="joseph"),
	path("daniel", views.daniel, name="daniel"),

	path("<str:name>", views.greet, name="greet"),
	path("", views.index, name="index"),
	


]