from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.
def index(request):
    return redirect('/agenda/')
    
def lista_eventos(request):
    # usuario = request.user
    evento = Evento.objects.all()
    #Evento.objects.filter(usuario=usuario) # retorna apenas do usuario em questão
    #Evento.objects.all() retorna todos os campos (perigoso se houver muitos dados)
    #Evento.objects.get(nome do campo) retorna apenas um campo em especifico
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
