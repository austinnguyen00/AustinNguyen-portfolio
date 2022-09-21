from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
  return render(request=request, template_name='my_portfolio/index.html')

def post(request):
  return render(request=request, template_name='my_portfolio/post.html')

def chess_opening(request):
  return render(request=request, template_name='my_portfolio/chess_opening.html')

def data_skills(request):
  return render(request=request, template_name='my_portfolio/data_skills.html')