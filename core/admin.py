from django.contrib import admin

from .models import Cliente, Produto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "email", "cpf", "data_cadastro")
    search_fields = ("nome", "sobrenome", "email", "cpf")
    list_filter = ("nome", "sobrenome", "email", "cpf")


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "estoque", "disponivel")
    search_fields = ("nome", "preco", "estoque", "disponivel")
    list_filter = ("nome", "preco", "estoque", "disponivel")
