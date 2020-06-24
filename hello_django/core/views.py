from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requests):
    return HttpResponse("<h1>Hello World!</h1>")

def soma(requests, n1, n2):
    return HttpResponse(f'<h1>{n1} + {n2} = {n1+n2}</h1>')

def subtracao(requests, n1, n2):
    return HttpResponse(f'<h1>{n1} - {n2} = {n1-n2}</h1>')

def multiplicacao(requests, n1, n2):
    return HttpResponse(f'<h1>{n1} * {n2} = {n1*n2}</h1>')

def divisao(requests, n1, n2):
    try:
        dividir = n1 / n2
    except ZeroDivisionError:
        return HttpResponse("<h1>Impossível fazer divisão por 0</h1>")
    else:
        return HttpResponse(f'<h1>{n1} / {n2} = {dividir}</h1>')
    
