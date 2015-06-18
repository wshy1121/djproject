from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def hello(req):
	return HttpResponse("<h1>Hello World!</h1>")

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

	