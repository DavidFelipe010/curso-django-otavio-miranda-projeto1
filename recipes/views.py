from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name':'David F.'
    })


def sobre(request):
    return render(request, 'recipes/contato.html')


def contato(request):
    return HttpResponse('CONTATO')
