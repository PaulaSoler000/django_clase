from django.contrib import admin
from .models import Task, Todo, User

admin.site.register(Task)
admin.site.register(Todo)
admin.site.register(User)
