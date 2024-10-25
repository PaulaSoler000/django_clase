from django.urls import path
from .views import to_dos

urlpatterns = [
    path('', to_dos, name="to_dos")
]