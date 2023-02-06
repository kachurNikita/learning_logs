from django.urls import path
from . import views

# Local variables for learning_logs  app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics page (Topic page)
    path('topics/', views.topics, name='topics'),
    path('topics/(?P<topic_id>\d+)', views.topic, name='topic'),
    path('new_topic/$', views.new_topic, name='new_topic'),
    path('new_entry/(?P<topic_id>\d+)', views.new_entry, name='new_entry'),
    # path('edit_enry/(?P<entry_id\d+)'), views.edit_entry, name='edit_entry'),
]