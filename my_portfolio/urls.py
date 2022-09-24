from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path(route='', view=views.index, name='index'),
  
  # Portfolios
  path(route='chopen', view=views.chopen, name='chopen'),
  path(route='ausdask', view=views.ausdask, name='ausdask'),

]