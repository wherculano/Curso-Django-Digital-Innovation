- Criando o ambiente virtual

   *    `python -m venv .nomeDoAmbiente`

- Instalando o Django
    * `pip install django`

- Criando o projeto
    * `django-admin startproject nomeDoProjeto`

- Testando o projeto

    *  `cd nomeDoProjeto`
    *  `python manage.py runserver`

- Criando a app
    * `django-admin startapp nomeDaApp`

Após criar a app, ir no arquivo settings.py e adicionar a nova app.
``` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nomeDaApp',
]
``` 

Agora é necessário incluir a rota no arquivo urls.py e também importar o módulo views para poder chamar a função:
```
from nomeDaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nomeDaRota/',views.nomeDaFuncao)
]
```

Agora no arquivo views.py é necessário criar a função, com o mesmo nome que foi incluso no arquivo urls.py, que irá retornar o conteúdo nesta rota que foi criada.
Deve-se também importar o módulo `HttpResponse`
```
from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requests):
    return HttpResponse("Hello World!")
```
- A função `hello` irá retornar a mensagem no navegador.

#### FIM DA AULA 1 ####