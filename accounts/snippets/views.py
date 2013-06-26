# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.core.context_processors import csrf
from django.contrib.auth import get_user_model
from snippets.models import Snippet, UserSnippet
from django.contrib.sessions.models import Session

def snippets(request):
  if request.user.is_authenticated():
    allsnippets = Snippet.objects.all()
    return render(request, 'snippets.html', {'snippets': allsnippets})
  else:
    return render(request, 'auth.html', {'state': 'You must be signed in to view this page.', 'form' : AuthenticationForm()})
