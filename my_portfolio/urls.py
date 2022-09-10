from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path(route='', view=views.index, name='index'),
  
  # Portfolios
  path(route='post.html', view=views.post, name='post'),
  path(route='chess_opening.html', view=views.chess_opening, name='chess_opening'),

]