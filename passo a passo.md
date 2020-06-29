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

### Um pouco de Teoria
1. **Django-admin:** é o utilitário de linha de comando do Django para tarefas administrativas;
1. **Manage:** É um *wrapper* em volta do django-admin.    
Ele delega tarefas para o django-admin.    
É o responsável por colocar o pacote do projeto no *sys.path*.    
Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que então aponta para o arquivo settings.py.    
Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar o uso dos comandos do django-admin.py (comandos administrativos).
1. **WSGI:** Web Server Gateway Interface (Interface de porta de entrada do servidor web).    
É uma plataforma padrão para aplicações web em Python.    
O Django com o comando `startproject` inicia uma configuração WSGI padrão para que se possa executar sua aplicação web.    
Quando se inicia a aplicação Django com o comando `runserver` é iniciado um servidor de aplicação web leve. Esse servidor é especificado pela configuração WSGI_APPLICATION.    
1. **Settings:** É o responsável pelas configurações do Django.    
Nele eé possível configurar por exemplo apps, conexões com banco de dados, templates, time zone, cache, segurança, arquivos estáticos, etc.    
1. **URLs:** É um *Schema* de URL.   
É responsável por gerenciar as rotas das URLs, onde é possível configurar para onde cada rota será executada.    
É uma forma limpa e elegante para gerenciar as URLs.
1. **Views:** Responsável por processar e retornar uma resposta para o cliente que fez a requisição.
1. **Models:** Define o modelo de dados interiramente em Python.    
Faz a abstração dos objetos de banco para o Python, transformando todas as tabelas em classes e os acessos são feitos utilizando a linguagem Python, onde o Django realiza a transformação para SQL.
1. **Admin:** Interface administrativa gerada automaticamente pelo Django.    
Ele lê os metadados que estão nos models e fornce uma interface poderosa e pronta para a manipulação de dados.
1. **Static:** Responsável por armazenar os arquivos estáticos (CSS, Javascript, imagens, etc).
1. **Templates:** Responsável por armanezar os arquivos HTML.    
O diretório templates é o diretório padrão para armazenarmos todo o conteúdo HTML da nossa aplicação.

### Aula 02 ###
* Criando o projeto "agenda"    
`django-admin startproject agenda`    
`django-admin startapp core`    
* Criando as tabelas do banco    
`python manage.py migrate`    
* Criando o usuário    
`python manage.py createsuperuser --username nomeDoUsuario`    
Após este comando será solicitado o e-mail e senha do usuario criado.    
Criando um novo usuario com as opções *auth | user | can view user* e *can view group*, este usuário terá acesso a página, mas somente para visualização.      

### Miagração de Dados no Django.
- Para migração de dados no Django, é necessário que tenha classes criadas.
- Com as classes criadas, para migração é utilizado o comando *migrate*
- Também pode-se utilizar o comando *migrations* para criação de um arquivo de migração, sem a necessidade de migras "às cegas".
- Pode-se utilizar também o comando *sqlmigrate*, que ao invés de aplicar a migração, é gerado todo comando para que essa migração possa ser efetuada manualmente no banco de dados.    

Após a criação dos modelos no arquivo *models.py*, rodar o comando `python manage.py makemigrations nomeDaApp`    
O comando *migrate* não foi utilizado para não registrar de imediato no banco de dados e o nome da app foi adicionado para o comando "olhar" apenas para essa app.    
Com o comando `python manage.py sqlmigrate` é mostrado os comandos SQL que irão gerar toda a criação da tabela.    
Para aplicar as alterações/informações geradas no banco de dados, basta rodar o `python manage.py migrate nomeDaApp 0001`  (0001 é o arquivo gerado pelo *makemigrations*).    
Após concluir, é necessário fazer o registro do banco no Django-admin (admin.py)    
### FIM DA AULA 2 ###    

### AULA 3
1. ### Templates  
Django oferece no seu modelo de templates a capacidade de se utilizar expressões Python no HTML.    
Com isso é possível mostrar informações e realizar comando como IF e FOR:    
``` 
<ul>
    {% for evento in eventos %}
        <li>{{evento.titulo}} - {{evento.get_data_evento}}</li>     
    {% endfor %}
</ul>
```    
Neste projeto foram criadas paginas HTML na pasta **templates**, onde a página principal "herda" as outras "camadas" HTML dos outros arquivos (footer e header). Pois assim ambos sempre permanecerão "intactos" em futuras alterações no arquivo principal.

