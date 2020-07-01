from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    '''Home page'''
    return redirect('/agenda/')

def login_user(request):
    '''Pagina de login'''
    return render(request, 'login.html')

def submit_login(request):
    '''Efetua o login após clicar no botão Entrar'''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválido!")
    return redirect('/')

@login_required(login_url='/login/') # exige uma sessão ativa    
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    #Evento.objects.filter(usuario=usuario) # retorna apenas do usuario em questão
    #Evento.objects.all() retorna todos os campos (perigoso se houver muitos dados)
    #Evento.objects.get(nome do campo) retorna apenas um campo em especifico
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        # salvando no banco
        Evento.objects.create(titulo=titulo,
                                data_evento=data_evento,
                                descricao=descricao,
                                usuario=usuario)
    return redirect('/')
