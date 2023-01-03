from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path(route='', view=views.index, name='index'),
  
  # Portfolios
  path(route='chopen', view=views.chopen, name='chopen'),
  path(route='ausdask', view=views.ausdask, name='ausdask'),
  path(route='recotify', view=views.recotify, name='recotify'),
  path(route='wordfixerbot', view=views.wordfixerbot, name='wordfixerbot'),

]