
from django.urls import path
from .views import *
urlpatterns = [
    path('all', ListAllTasks),
    path('new',AddTask)
]
