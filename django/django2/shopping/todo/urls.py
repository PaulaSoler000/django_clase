from django.urls import path
from .views import index, add
from .views import create_form

urlpatterns = [
    path('', index, name="todo.index"),
    path('add/', add, name='todo.add'),
    path('create_form/', create_form, name='todo.create_form'),
]

