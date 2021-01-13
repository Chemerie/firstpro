from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greet(request, name):
	return render(request, "hello/greet.html", {
		"name": name.capitalize()
		})

def index(request):
	return render(request, "hello/index.html")

def joseph(request):
	return HttpResponse("Hello Joseph")

def daniel(request):
	return HttpResponse("Hello Daniel")
