from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book

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

