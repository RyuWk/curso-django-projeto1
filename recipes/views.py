from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', {
        'name':'RyuWk'
    })


def teste(request):
    return HttpResponse('Teste2')


def contato(request):
    return HttpResponse('Contatos2')
