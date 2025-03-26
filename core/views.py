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
    # print(request)
    print(request.user)
    # print(request.user.is_authenticated)
    # print(request.user.username)
    # print(request.user.email)
    # print(request.user.get_full_name())
    # print(request.user.get_short_name())

    if request.user.is_authenticated:
        print("Usuário autenticado")
    else:
        print("Usuário não autenticado")

    context = {
        "curso": "Programação WEB com Django Framework",
        "empresa": "Geek University",
        "instrutor": "José da Silva",
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")
