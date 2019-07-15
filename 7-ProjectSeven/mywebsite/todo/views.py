from django.shortcuts import render, redirect

# Create your views here.
from .forms import TodoForm
from .models import Todo


def index(request):
    
    return render(request, 'index.html')

