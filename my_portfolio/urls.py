from django.urls import path
from . import views

urlpatterns = [

  # Home page
  path(route='', view=views.index, name='index'),
  
  # Portfolios
  path(route='post.html', view=views.post, name='post'),
  path(route='chess_opening.html', view=views.chess_opening, name='chess_opening'),
  path(route='data_skills.html', view=views.data_skills, name='data_skills'),

]