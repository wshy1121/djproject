from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from forms import ContactForm
from forms import PublisherForm
# Create your views here.

def search(request):
	query = request.GET.get('q', '')
	print query
	if query:
		qset = (
		Q(title__icontains=query) |
		Q(authors__first_name__icontains=query) |
		Q(authors__last_name__icontains=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []

	return render_to_response("search.html", {
	"results": results,
	"query": query
	})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic = form.cleaned_data['topic']
			message = form.cleaned_data['message']
			sender = form.cleaned_data.get('sender', 'noreply@example.com')
			send_mail(
				'Feedback from your site, topic: %s' % topic, message, sender,
				['huangyuan1@hikvision.com.cn']
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm()
	return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))



def add_publisher(request):
	if request.method == 'POST':
		form = PublisherForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_publisher/thanks/')
	else:
		form = PublisherForm()
	return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))

