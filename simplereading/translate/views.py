from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Simple, Original, History
from .forms import OriginForm, SimpForm, TestForm
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
    form = TestForm(initial={'original_text': hard_text})
    if 'original_text' in request.GET and request.GET["original_text"]:
        hard_text = request.GET.get("original_text")
        return redirect('result', hard_text)
    else:
        return render(request, 'result.html', {'hard_text': utils.simplify(hard_text), 'form' : form})


def contribute(request):
    origins = Original.objects.all()
    return render(request, 'contribute.html', {'origins' : origins })


def add_simp(request, pk):
    orig = Original.objects.get(pk=pk)
    form = SimpForm()
    results = Simple.objects.filter(hard=pk)
    simple_text = request.POST.get("simple_text")
    if request.method =="POST":
        save_form = SimpForm(request.POST)
        if save_form.is_valid():
            simp = save_form.save(commit=False)
            simp.simple_text = simple_text
            simp.hard = orig
            simp.save()
        return render(request, 'add_simp.html', {'results': results, 'orig' : orig, 'form': form })
    else:
        return render(request, 'add_simp.html', {'results': results, 'orig' : orig, 'form': form})


def edit_simp(request, pk):
    simp = Simple.objects.get(pk=pk)
    form = SimpForm(initial={'simple_text': simp.simple_text})
    new_simple_text = request.POST.get("simple_text")
    if request.method =="POST":
        simp.simple_text = new_simple_text
        simp.save()
        return redirect('add_simp', simp.hard.id )
    else:
        return render(request, 'edit_simp.html', {'form' : form})

def add_origin(request):
    hard_text = request.POST.get("hard_text")
    if request.method =="POST":
        save_form = OriginForm(request.POST)
        if save_form.is_valid():
            orig = save_form.save(commit=False)
            orig.hard_text = hard_text
            orig.save()
            origins = Original.objects.all()
        return redirect('contribute')
    else:
        form = OriginForm()
        return render(request, 'add_origin.html', { 'form':form })

