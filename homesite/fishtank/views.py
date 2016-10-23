from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Temperature
# Create your views here.

def index(request):
	temps = Temperature.objects.all()
	template = loader.get_template('fishtank/index.html')
	context = {
		'temps':temps,
	}
	return HttpResponse(template.render(context,request))
