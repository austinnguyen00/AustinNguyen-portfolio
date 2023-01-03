from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
  return render(request=request, template_name='my_portfolio/index.html')

def chopen(request):
  return render(request=request, template_name='my_portfolio/chopen')

def ausdask(request):
  return render(request=request, template_name='my_portfolio/ausdask')

def recotify(request):
  return render(request=request, template_name='my_portfolio/recotify')

def wordfixerbot(request):
  return render(request=request, template_name='my_portfolio/wordfixerbot')