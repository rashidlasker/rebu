from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("aye lmao")
	# template = loader.get_template('polls/index.html')
	# context = {}
 #    return render(request, 'polls/index.html', context)