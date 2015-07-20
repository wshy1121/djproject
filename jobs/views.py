# -*- coding: UTF-8 -*- 

from django.shortcuts import render
from django.template.loader import get_template
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


def template(req):
	#模板的简单使用
	tempText = 	"""
			<html>  
			<head><title>Ordering notice</title></head>  
			<body>  
			<p>Dear {{ person_name }},</p>  
			<p>Thanks for placing an order {{ product }} from {{ company }}. It's scheduled to  
			ship on {{ ship_date|date:"F j, Y" }}.</p>  
			<p>Here are the items you've ordered:</p>  
			<ul>  
			{% for item in item_list %}  
			<li>{{ item }}</li>  
			{% endfor %}  
			</ul>  
			{% if ordered_warranty %}  
			<p>Your warranty information will be included in the packaging.</p>  
			{% endif %}  
			<p>Sincerely,<br />{{ company }}</p>  
			</body>  
			</html>  
			"""
	t = Template(tempText)

	c = Context({'person_name': 'John Smith',  
	     'product': 'Super Lawn Mower',  
	     'company': 'Outdoor Equipment',  
	     'ship_date': datetime.date(2009, 4, 2),  
	     'item_list': ["111", "222"],
	     'ordered_warranty': True
	     })  

	return HttpResponse(t.render(c))



def current_datetime(req):
	now = datetime.datetime.now()

	t = get_template('mytemplate.html')

	c = Context({"current_date":now})

	html = t.render(c)
	return HttpResponse(html)