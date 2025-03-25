from django.shortcuts import render


"""
Nota do aluno:
Após criar a aplicação o primeiro passo é criar a pasta templates na raiz da aplicação. 
Dentro dessa pasta para em seguida criar os os métodos views que serão responsáveis 
por renderizar as páginas HTML do arquivo chamado:
    index.html
    contato.html
"""


def index(request):
    return render(request, "index.html")


def contato(request):
    return render(request, "contato.html")
