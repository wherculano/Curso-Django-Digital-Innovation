from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

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
    data_atual = datetime.now() - timedelta(hours=1) # considerando evento 1h atrasado
    evento = Evento.objects.filter(usuario=usuario,
                                    data_evento__gt=data_atual)
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
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        local = request.POST.get('local')
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.user == usuario:
                evento.titulo=titulo
                evento.data_evento=data_evento,
                evento.descricao=descricao,
                evento.local=local
                evento.save()
             #Evento.objects.filter(id=id_evento).update(titulo=titulo,
             #                       data_evento=data_evento,
             #                       descricao=descricao,
             #                       local=local) # esta comando faz a mesma coisa que o if acima, atualiza os campos
        else:
        # salvando no banco
            Evento.objects.create(titulo=titulo,
                                    data_evento=data_evento,
                                    descricao=descricao,
                                    usuario=usuario,
                                    local=local)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete() # excluindo o evento por id
    else:
        raise Http404()
    return redirect('/')

# @login_required(login_url='/login/') # comentar para criar api publica que não requer login
def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario) # liberando todos os usuarios por id em uma api publica
    #usuario = request.user # inserir e remover a linha acima, será api privada
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo', 'local','descricao')
    return JsonResponse(list(evento), safe=False) # safe é por passar uma lista e não um dicionário
