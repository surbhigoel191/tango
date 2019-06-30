from django.shortcuts import render
from django.http import HttpResponse
def index(request): 
	htmla="Rango says hello world!" + '<a href = "/rango/about">About</a>'
	return HttpResponse(htmla)
def about(request): 
	htmlb="Rango Says: Here is the about page." + '<a href = "/rango">Index</a>'
	return HttpResponse(htmlb)