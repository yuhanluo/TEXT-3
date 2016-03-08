from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Simple, Original, History
from .forms import SimplifyForm, TestForm
from django.core.urlresolvers import reverse
import functions, utils


def index(request):

    if 'original_text' in request.GET and request.GET["original_text"]:
        hard_text = request.GET.get("original_text")
        return redirect('result', hard_text)
    else:
        form = TestForm()
        return render(request, 'index.html', {'form' : form})


def result(request, hard_text):
    form = TestForm()
    if 'original_text' in request.GET and request.GET["original_text"]:
        hard_text = request.GET.get("original_text")
        return redirect('result', hard_text)
    else:
        return render(request, 'result.html', {'hard_text': utils.simplify(hard_text), 'form' : form})
