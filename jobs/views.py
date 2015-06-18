from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
import datetime

def hello(req):
	t = Template("<h1>Hello World! My name is {{my_name}}.</h1>") 
	c = Context({"my_name": "Stephane"})  
	
	return HttpResponse(t.render(c))

def homepage(req):
	return HttpResponse("<h1>this is homepage!</h1>")

def ctime(req, num):
	try:
		num=int(num)
		num=str(num)
	except ValueError:
		raise Http404

	cutime = datetime.datetime.now()
	txt = "it is %s" % cutime

	print num

	return HttpResponse(txt) 

	