from django.shortcuts import render

# Create your views here.
def to_dos(request):
    return render(request, 'to_dos.html')