from django.contrib import admin
from learning_logs.models import Topic
from learning_logs.models import Entry


# Register your models here.
# Importing topic model, then tell Django to manage our model trough admin site
admin.site.register(Topic)
admin.site.register(Entry)
