from django.shortcuts import render
from django.http import HttpResponse
from .models import Simple, Original, translation

def index(request):
       return render(request, 'index.html')

def result(request):
       return render(request, 'result.html')

