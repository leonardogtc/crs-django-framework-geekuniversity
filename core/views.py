from django.shortcuts import render
from .models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        "curso": "Programação WEB com Django Framework",
        "empresa": "Geek University",
        "instrutor": "José da Silva",
        "produtos": produtos,
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")


def produto(request, id):
    produto = Produto.objects.get(id=id)
    context = {"produto": produto}
    return render(request, "produto.html", context)
