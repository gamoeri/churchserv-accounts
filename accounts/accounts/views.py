from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def home(request):
  if request.user.is_authenticated():
      return render(request,'home.html', RequestContext(request))
  else:
      return render(request, 'auth.html', {'state': 'You must be signed in to view this page.', 'form' : AuthenticationForm()})

def hello(request):
	return HttpResponse("Hello World")
	
def index(request):
	return render(request, 'index.html')

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is %s. </body</html>" % now
	return HttpResponse(html);
