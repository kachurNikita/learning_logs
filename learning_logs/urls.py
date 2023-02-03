from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics page
    path('topics/', views.topics, name='topics')

]