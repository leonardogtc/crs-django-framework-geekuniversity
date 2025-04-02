from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader


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
    # produto = Produto.objects.get(id=id)
    produto = get_object_or_404(Produto, id=id)
    context = {"produto": produto}
    return render(request, "produto.html", context)


def erro404(request, exception):
    template = loader.get_template("404.html")
    return HttpResponse(
        content=template.render(), content_type="text/html; charset=utf8", status=404
    )  # Retorna o template com status 404


def erro500(request):
    template = loader.get_template("500.html")
    return HttpResponse(
        content=template.render(), content_type="text/html; charset=utf8", status=500
    )  # Retorna o template com status 500
