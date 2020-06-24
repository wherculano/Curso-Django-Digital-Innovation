from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requests):
    return HttpResponse("<h1>Hello World!</h1>")
    # return HttpResponse("<h1>Hello <nome> de <idade> anos!</h1>")
    # nome e idade são parametros da url que serão recebidos aqui na função e renderizados
    
