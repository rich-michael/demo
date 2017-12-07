from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.

def about(request):
	template = get_template('about.html')
	html = template.render()
	
	return HttpResponse(html)

def index(request):
	template = get_template('index.html')
	html = template.render()	
	return HttpResponse(html)
